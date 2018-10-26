# A3C Blog Post
In order to run this code, you will need the following prerequisites:

* [OpenAI Gym](https://github.com/openai/gym) - `pip install gym`
* pyglet - `pip intall pyglet` 
* [TensorFlow](https://www.tensorflow.org/install/) - `pip install tensorflow`

## instructions for running this file

* First step is training.

  * If you want to run this from command line, then run `python a3c_cartpole.py --algorithm=a3c --train --max-eps=1000`.

  * If you want to use PyCharm to debug and understand the code, then replace the code
`args = parser.parse_args()` in the a3c_cartpole.py with `args = parser.parse_args(['--algorithm', 'a3c', '--train', '--max-eps', '400'])`. If you are using Windows, then there is a possiblity that your trained model h5 file will be saved to a location relative to your drive root directory. So you can also specify it as an absolute directory. For example, I used the following code:

```
args = parser.parse_args(['--algorithm', '--train', 'a3c', '--max-eps', '400', '--save-dir', "E:/Repos/Tensorflow/tensorflow-research-api-zh/tmp/"])
```

* Second step is to test your model. Get rid of the '--train' in the command line, and you can see how well the pole is moving with respect to the cart.
