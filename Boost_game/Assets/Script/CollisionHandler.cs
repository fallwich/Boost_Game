using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
public class CollisionHandler : MonoBehaviour
{
    [SerializeField] float levelLoadDelay = 2f;
    void OnCollisionEnter(Collision other) 
    {
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
        GetComponent<Movement>().enabled = false;
        Invoke("LoadNextLevel", levelLoadDelay);
    }

    void StartCrashSequence()
    {
        GetComponent<Movement>().enabled = false;
        //장애물에 닿으면 Rocket의 제어권을 false 시키고 시작 지점으로 돌아간다.
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
