using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class CollisionHandler : MonoBehaviour
{
    [SerializeField] float levelLoadDelay = 2f;
    [SerializeField] AudioClip success;
    [SerializeField] AudioClip crash;

    [SerializeField] ParticleSystem successParticle;
    [SerializeField] ParticleSystem crashParticle;
    AudioSource audioSource;
    bool collisionDisabled = false;
    bool isTransitioning = false;
    private void Start() 
    {
        audioSource = GetComponent<AudioSource>();
    }
    void Update() 
    {
        RespondToDebugKeys();
    }
    void RespondToDebugKeys()
    {
        if (Input.GetKeyDown(KeyCode.L))
        {
            LoadNextLevel();
        }
        else if(Input.GetKeyDown(KeyCode.C))
        {
            collisionDisabled = !collisionDisabled; //toggle collision 토글한다.
            if(collisionDisabled == false)
            {
                Debug.Log("false");
            }
            else
            {
                Debug.Log("true");
            }
        }
    }
    void OnCollisionEnter(Collision other) 
    {
        if (isTransitioning || collisionDisabled) {return;}
        //장애물이나 도착 지점에 갔을 때 isTransitioning이 true로 변하고
        //true면 아무것도 하지 않는다. false인 상태에서 swithch문을 실행하기 때문에
        //sound와 재시작, 다음 Scene으로 넘어가고 sound가 겹치지 않게 된다.
        switch (other.gameObject.tag)
        {
            case "Friendly":
                Debug.Log("This thing is friendly");
                break;
            case "Finish":
                StartSuccessSequence();
                break;
            default:
                StartCrashSequence();
                break;
        }
    }

    void StartSuccessSequence() // Finish에 도착하면 다음 Scene으로 이동 Rocket은 잠시 못움직임.
    {
        isTransitioning = true;
        audioSource.Stop();
        audioSource.PlayOneShot(success);
        GetComponent<Movement>().enabled = false;
        successParticle.Play();
        Invoke("LoadNextLevel", levelLoadDelay);
    }

    void StartCrashSequence()
    {
        isTransitioning = true;
        audioSource.Stop();
        audioSource.PlayOneShot(crash);
        GetComponent<Movement>().enabled = false;
        //장애물에 닿으면 Rocket의 제어권을 false 시키고 시작 지점으로 돌아간다.
        crashParticle.Play();
        Invoke("ReloadLevel", levelLoadDelay);
    }
    void ReloadLevel()
    {
        int currentSceneIndex = SceneManager.GetActiveScene().buildIndex;
        SceneManager.LoadScene(currentSceneIndex);
        //반환될 인덱스(Scene의 인덱스)를 현재 활동하고 있는 씬의 인덱스를 반환
    }

    void LoadNextLevel()
    {
        int currentSceneIndex = SceneManager.GetActiveScene().buildIndex; //현재 Scene의 Index
        int nextSceneIndex = currentSceneIndex + 1;
        if (nextSceneIndex == SceneManager.sceneCountInBuildSettings)
        //SceneManager.sceneCountInBuildSettings 총 Scene의 갯수
        {
            nextSceneIndex = 0;
        }
        SceneManager.LoadScene(nextSceneIndex);
    }
    //Invoke 메서드가 X초 동안 지연된 이후 실행되게 할 수 있다.
    //Invoke("MethodName", delayInSeconds);
}
