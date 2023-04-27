# Talk-2-ChatGPT

<< Purpose >> Code project to demonstrate setting up a simple app for having a conversation with OpenAI ChatpGPT innovation. The idea is to show that using simple APIs the interaction can ve multi-modal out-of-the-box

<< Description >> This is demonstrations using a rudimentary application written in few lines of code to demonstrate the very human like conversation with and AI Language model. In this case ChatGPT. 
The benefits maybe limitless including improved productivity and accessibility. The code iteslf has been developed using the GitHub Copilot, including
the profuse comments to make the reading and understanding of this short code. This is a short code, but this copilot assisted commenting
is a huge productivity gain for developers. Saving their time to focus on the code logic and features, without sacrificing the readability and
the ease of maintenance of the code itself.

Here is a short ~4 minutes video depicting the expereince of talking to OpenAI ChatGPT model in a youTube video :
https://youtu.be/uVrhM3Tmlvw

<< Installation Steps >>
1. Download the code to your Windows Device
2. Ensure your Windows device is setup for running the Python .py program file
3. Launch the "talk-2-chatgpt.py" program file.
4. Click on the local http:// URL that this program provides, which may take a few seconds.

<< Using the App >>
1. Click on recording button.
2. Record your query.
3. Stop recording.
4. Submit recording.

<< Workflow of the system >> 
The Program GUI will capture your speech query. It store this speech in a audio file locally on your windows device. The program will send this audio file to OpenAI Wisper API for using the speech-to-text conversation AI model services. Upon receving this converted response from th eWisper AI model, this program will store the message in a message array. The agrregated array members together will form the input prompt that this progrma will not send to the OpenAI ChatGPT-n model. The reponse rececived from the ChatGPT-n model is appended to the same message array referred to in the previous sentences. This progressively aggregating conversation, enables ChatGPT to main the all important context of the on-going conversation. Additianlly, the immediate response is converted back to speech using google GTTS (text-to-speech) library and read back to the user thorugh the Windows device speaker. Also the entire prompt text that is progressively growing is printed in the app on the text box on the right for user reading reference.
