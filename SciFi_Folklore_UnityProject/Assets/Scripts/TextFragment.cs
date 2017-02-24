using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TextFragment : MonoBehaviour {

	public TextMesh txt;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	public void SetText(string s)
	{
		txt.text=s;
	}
}
