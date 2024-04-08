
from util import manhattanDistance
from game import Directions
import random, util
from game import Agent

class ReflexAgent(Agent):
    
    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"


        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
      
      # Extract useful information from the current game state
      newPos = currentGameState.getPacmanPosition()
      newFood = currentGameState.getFood()
      newGhostStates = currentGameState.getGhostStates()
      newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

      # Initialize evaluation score
      evalScore = currentGameState.getScore()

      # Calculate reciprocal of distance to the nearest food pellet
      foodDistances = [manhattanDistance(newPos, foodPos) for foodPos in newFood.asList()]
      if foodDistances:
          evalScore += 1.0 / min(foodDistances)

      # Evaluate ghost positions
      for ghostState, scaredTime in zip(newGhostStates, newScaredTimes):
          ghostPos = ghostState.getPosition()
          distToGhost = manhattanDistance(newPos, ghostPos)
          if scaredTime == 0:
              if distToGhost < 2:
                  evalScore -= 10  # Penalize if too close to a non-scared ghost
          else:
              evalScore += 100 / (distToGhost + 1)  # Encourage chasing scared ghosts

      return evalScore

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      In process
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      In process minimax agent
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

