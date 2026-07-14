using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;

public class EndSceneManager : MonoBehaviour
{
    public TMP_Text scoreText;

    void Start()
    {
        int pop = ResultData.FinalPopulation;
        float satis = ResultData.FinalSatisfaction;

        int finalScore = Mathf.RoundToInt(pop * satis);

        Logger.Log($"Final Population: {pop}, Satisfaction: {satis:F2}, Final Score: {finalScore}");

        scoreText.text = "Your final score is : " + finalScore;
    }

    public void BackToMainMenu()
    {
        SceneManager.LoadSceneAsync(SceneName.StartScene.ToString());
    }

    public void RetryGame()
    {
        SceneManager.LoadSceneAsync(SceneName.MainScene.ToString());
    }
}