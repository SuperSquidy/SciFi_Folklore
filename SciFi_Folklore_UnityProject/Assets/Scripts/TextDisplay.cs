using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/*
	Activated by a trigger volume.
	Show the next line of text in the "walkthrough."

*/


public class TextDisplay : MonoBehaviour {
	TextDisplayManager textManager;
	public GameObject textFragmentPrefab;

	void Start () {
		textManager=TextDisplayManager.instance;

	}
	
	void Update () {
				
	}

	void OnTriggerEnter(Collider other)
	{
		if (other.gameObject.tag == "Player")
		{
			string s=textManager.GetRandomFragment();
			Debug.Log(s);
			GameObject g =  Instantiate (textFragmentPrefab, transform.position, transform.rotation);
			TextFragment tf = g.GetComponent<TextFragment>();
			tf.SetText(s);
			Destroy(g,3.0f);
		}

	}


}
