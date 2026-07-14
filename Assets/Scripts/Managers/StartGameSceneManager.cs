using UnityEngine;
using UnityEngine.SceneManagement;

public class StartGameSceneManager : MonoBehaviour
{
    private string MainSceneName = "MainScene";

    public void PlayGame(){
        SceneManager.LoadSceneAsync(MainSceneName); 
    }

    public void QuitGame(){
        Logger.Log("Quitting the game...");  
        Application.Quit();
    }
}
