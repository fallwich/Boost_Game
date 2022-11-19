# Boost_Game 오류 및 공부
OmniSharp.MSBuild.ProjectLoader         .NETFramework,Version=v4.7.1의 참조 어셈블리를 찾을 수 없습니다.

오류가 발생 - Vscode에서 Unity Class가 자동완성이 안됨.

.Net framework, Version 4.7.1 Developer Pack 다운으로 해결.

https://dotnet.microsoft.com/en-us/download/dotnet-framework/thank-you/net471-developer-pack-offline-installer


https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.LoadScene.html - SceneManager


public static void LoadScene(int sceneBuildIndex, SceneManagement.LoadSceneMode mode = LoadSceneMode.Single);


현재 씬을 가져올 수 있는 LoadScene


using UnityEngine.SceneManagement; using 해야 사용 가능

SceneManager.GetActiveScene().buildIndex 현재 Scene Index

SceneManager.sceneCountInBuildSettings 총 Scene의 수


Invoke 메서드가 X초 동안 지연된 이후 실행되게 할 수 있다.


Invoke("MethodName", delayInSeconds);

AudioSource audioSource; - cache 캐싱 가독성이나 속도가 빠르게 처리 가능.

audioSource.Play() -- 효과음이 하나일 때 효과적.

audioSource.PlayOneShot() -- 여러개의 효과음 사용 가능.

audioSource.Stop() -- 진행중인 효과음 중단.

ParticleSystem.Play() --particle 실행.

Looping -오디오와 비슷하게 파티클이 계속 실행(부스트 시 사용), Play On Awake -게임 시작시 바로 실행.

Movement Factor - 0: 움직이지 않음, 1: 움직임

Offset = Movement Factor * Moverment Vector

Mathf.Sin - radians에 값을 넣으면 -1 ~ 1 사이의 값이 나온다.

Mathf.Epsilon - float에서 가장 작은 수, float 수를 비교할 때 정확히 같을 수가 없다.

그러므로 Epsilon을 사용하여 오차 범위를 설정해야 한다.

배경 꾸미는 법 - Material - Lighting - skybox Material에서 선택

Inspector에서 shader - standard - skybox - procedural 변경.
