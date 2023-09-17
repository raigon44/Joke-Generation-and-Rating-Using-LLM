# Joke-Generation-and-Rating-Using-LLM
Within this repository, you will find code for a humor-oriented bot. This bot has the ability to produce various categories of jokes and can also assess the quality of jokes.

### Objective 
Following are the objective of this project:
  - Finetune a large language model for joke generation.
  - Finetune a large language model to assess the quality of a joke.
  - Create an interactive humor-oriented bot which is capable of generating jokes from different genre.

This project was done as part of the [AI Comedy Club Challenge](https://github.com/konfuzio-ai/ai-comedy-club).
### Steps to replicate the Bot

#### Install Dependencies

<pre>
pip install -r requirements.text
</pre>

All the configuration need for data loading, data cleaning, model training, model inference and so on are stored in the below file. <pre> src/config.py </pre>

#### Running the Bot

Run the below command to start interacting with the bot.

<pre>
python src/joke_bot.py
</pre>

The joke bot can be run directly without the need for training the joke-generator and joke-rater model. I have uploaded my trained models to [HuggingFace](https://huggingface.co/raigon44). While inference, the joke-bot will use these models. Links to the models are provided below:

[Joke Generator Model](https://huggingface.co/raigon44/iTellJokes)

[Joke Rater Model](https://huggingface.co/raigon44/iRateJokes)

Incase if you want to fine-tune the models again, please follow the below steps.

#### Train the joke generator and joke rater modesls

As mentioned before, all the hyperparameters necessary for model finetuning is stored in the *src/config.py* file. Adapt the necessary hyperparmeters by editing this file before fine-tuning the models.
After adjusting the hyperparametes, run the below command to fine-tune the models.

<pre>
python src/train_models.py
</pre>

### Dataset

In this section we will discuss the dataset used for model training and the preprocessing steps done.

#### About rjokes dataset
rJokes Dataset [1]: a collection of over 550,000 jokes posted over an 11-year period on the Reddit r/Jokes subreddit channel. This dataset also provides quantitative metrics for the level of humor (0 - 11) in each joke, determined by subreddit user feedback (upvoted and downvoted).

After the exploration of the dataset, for this challenge, I am only planning to use jokes with labels from 1 to 10.

[1](https://aclanthology.org/2020.lrec-1.753)

GitHub link to download the dataset: [https://github.com/orionw/rJokesData/tree/master/data](https://github.com/orionw/rJokesData/tree/master/data)

#### Data Preprocessing

The dataset underwent the following preprocessing steps:

- Removed special characters 
- Removed emojis
- Removed jokes which have less than 5 words
- Removed toxic jokes using Google's perspective API

### Models used

### User interaction

