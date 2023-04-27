# Talk-2-ChatGPT

<< Purpose >> Code project to demonstrate setting up a simple app for having a conversation with OpenAI ChatGPT innovation. The idea is to show that using available APIs a multi-modal interactive experience can be easily developed.

<< Description >> This is a demonstration using a rudimentary application written in few lines of Python code to demonstrate the very human like conversation with the AI Language model is possible, in this case ChatGPT. The benefits maybe limitless including improved productivity and accessibility. The code itself has been developed using the GitHub Co-pilot, including the profuse comments to make the reading and understanding of this short code significantly more friendly. This is a short code, but this Co-pilot assisted coding and commenting is a huge productivity gain for developers. Saving their time to focus on the code logic and features, without sacrificing the readability and the ease of maintenance of the code itself.

Here is a short ~4 minutes video depicting the experience of talking to OpenAI ChatGPT model in a YouTube video :
[![YouTube Video](readme-video-thumb.png?raw=true "YouTube video")] https://youtu.be/uVrhM3Tmlvw

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
The Program GUI will capture your speech query. It stores this speech in a audio file locally on your windows device. The program will send this audio file to OpenAI Wisper API for using the speech-to-text conversation AI model services. Upon receiving this converted response from the Wisper AI model, this program will store the message in a message array. The aggregated array members together will form the input prompt that this program will not send to the OpenAI ChatGPT-n model. The response received from the ChatGPT-n model is appended to the same message array referred to in the previous sentences. This progressively aggregating conversation enables ChatGPT to main the all-important context of the on-going conversation. Additionally, the immediate response is converted back to speech using google GTTS (text-to-speech) library and read back to the user through the Windows device speaker. Also the entire prompt text that is progressively growing is printed in the app on the text box on the right for user reading reference.

<< END >>
