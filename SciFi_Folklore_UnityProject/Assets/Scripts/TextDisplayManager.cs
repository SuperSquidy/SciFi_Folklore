using System.Collections;
using System.Collections.Generic;
using UnityEngine;


/* 

	load the whole text, split it (into lines, paragraphs, or just number of words or characters)

	returns the next text fragment when called 


*/

public class TextDisplayManager : MonoBehaviour {

	public TextAsset[] textAssets;

	public static TextDisplayManager instance; 

	string[] textFragments; 

	int currentFragment=-1;

    void Awake()
    {
        if (instance == null)
            instance = this;
        
        else if (instance != this)
            Destroy(gameObject);    
        
        DontDestroyOnLoad(gameObject);
    }

	void Start () {
		// process all the text assets 

		string allText="";

		for (int i=0;i<textAssets.Length;i++)
		{
			allText += textAssets[i].text;

		}

		char[] delimiters = {'.','!','?'};
		// split into sentences on punctuation.
		textFragments = allText.Split(delimiters);

		Debug.Log(textFragments.Length);
	}
	
	void Update () {
		
	}

	// return the next text fragment in order 
	public string GetNextFragment()
	{
		currentFragment++;
		if (currentFragment>=textFragments.Length) 
			currentFragment=0;
		return textFragments[currentFragment];
	}

	// return a fragment at random
	public string GetRandomFragment ()
	{
		currentFragment=(int)Random.Range(0,textFragments.Length);
		return textFragments[currentFragment];

	}
}
