using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Oscillator : MonoBehaviour
{
    Vector3 startingPosition;
    [SerializeField] Vector3 movementVector;
    float movementFactor;
    [SerializeField] float period = 2f;

    void Start()
    {
        startingPosition = transform.position;
    }

    void Update()
    {
        if (period <= Mathf.Epsilon) { return;}
        const float tau = Mathf.PI * 2;
        float cycles = Time.time / period; //지난 시간  주기, 만약 주기가 2라면 1 cycle은 2초
        float sinWave = Mathf.Sin(cycles * tau); // -1 ~ 1 사이의 값
        movementFactor = (sinWave + 1f) / 2f; // 1 더해서 (0 ~ 2)에서 2 나눠서 0 ~ 1 사이 
        Vector3 offset = movementVector * movementFactor;
        transform.position = startingPosition + offset;
    }
}
