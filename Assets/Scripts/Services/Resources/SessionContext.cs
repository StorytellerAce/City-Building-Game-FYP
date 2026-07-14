using System;
using UnityEngine;
using TMPro;

public class SessionContext
{
    private TMP_Text sessionIdText;
    public string SessionId { get; private set; }
    public bool HasSession => !string.IsNullOrEmpty(SessionId);

    public event Action<string> OnSessionStarted;

    public SessionContext(TMP_Text sessionIdText)
    {
        this.sessionIdText = sessionIdText;
        SessionId = null;
    }

    public void SetSessionId(string sessionId)
    {
        SessionId = sessionId;
        OnSessionStarted?.Invoke(sessionId);
        Logger.Log($"Session started with ID: {sessionId}");
        if (sessionIdText != null)
        {
            sessionIdText.text = $"Session ID: {sessionId}";
        }
    }

    public void Clear()
    {
        SessionId = null;
    }
}