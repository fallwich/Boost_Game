using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour
{
    [SerializeField] float mainThrust = 100f; //매개변수 편집기에서 수정 가능하다.
    [SerializeField] float rotationThrust = 1f;
    [SerializeField] AudioClip mainEngine;
    [SerializeField] ParticleSystem mainEngineParticels;
    [SerializeField] ParticleSystem rightThrusterParticels;
    [SerializeField] ParticleSystem leftThrusterParticels;
    Rigidbody rb; // rb = rigidbody //cache 캐싱 가독성이 좋다.
    AudioSource audioSource;
    ParticleSystem boost;
    
    bool isAlive;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        audioSource = GetComponent<AudioSource>();
        boost = GetComponent<ParticleSystem>();
    }

    // Update is called once per frame
    void Update()
    {
        ProcessThrust();
        ProcessRotation();
    }

    void ProcessThrust()
    {
        if (Input.GetKey(KeyCode.Space))
        {
            StartThrusting();
        }
        else
        {
            StopThrusting();
        }
    }
    void ProcessRotation()
    {
        if (Input.GetKey(KeyCode.A))
        {
            RotateLeft();
        }
        else if (Input.GetKey(KeyCode.D))
        {
            RotateRight();
        }
        else
        {
            StopRotating();
        }
    }
    void StartThrusting()
    {
        rb.AddRelativeForce(Vector3.up * mainThrust * Time.deltaTime);
        //프레임율에 영향을 받지 않게 Time.deltaTime(알아서 계산 해주는 함수)을 사용
        if (!audioSource.isPlaying)
        {
            audioSource.PlayOneShot(mainEngine); //audioSource.Play는 효과음이 하나일 때 효과적이다.
                                                 // AudioSource.PlayOneShot은 여러개의 효과음 사용 가능.
        }
        if (!mainEngineParticels.isPlaying)
        {
            mainEngineParticels.Play();
        }
    }
    void StopThrusting()
    {
        audioSource.Stop();
        mainEngineParticels.Stop();
    }
    private void StopRotating()
    {
        rightThrusterParticels.Stop();
        leftThrusterParticels.Stop();
    }

    private void RotateRight()
    {
        ApplyRotation(-rotationThrust);
        if (!leftThrusterParticels.isPlaying)
        {
            leftThrusterParticels.Play();
        }
    }
    private void RotateLeft()
    {
        ApplyRotation(rotationThrust);
        if (!rightThrusterParticels.isPlaying)
        {
            rightThrusterParticels.Play();
        }
    }
    public void ApplyRotation(float rotationThisFrame)
    {
        rb.freezeRotation = true; // 수동 제어를 위한 회전 고정
        transform.Rotate(Vector3.forward * rotationThisFrame * Time.deltaTime);
        rb.freezeRotation = false; // 물리 시스템이 적용 되도록 회전 고정 헤제
    }
}
