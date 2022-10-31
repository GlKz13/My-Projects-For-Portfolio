
const totalScore = {
    'computerScore': 0,
    'playerScore': 0

}

function getComputerChoice() {
    const rpsChoices = ['rock', 'paper', 'scissors']
    const randomChoice = Math.floor(Math.random() * 3)
    return rpsChoices[randomChoice]
}

console.log(getComputerChoice())

function getResult(playerChoice, computerChoice) {
    let score
    if (playerChoice == computerChoice) {
         score = 0
    } else if (playerChoice == 'rock' && computerChoice == 'scissors') { score = 1 }
    else if (playerChoice == 'paper' && computerChoice == 'rock') { score = 1 }
    else if (playerChoice == 'scissors' && computerChoice == 'paper') { score = 1 }
    else { score = -1}

    return score
}

function showResult(score, playerChoice, computerChoice) {
    const resultDiv = document.getElementById('result')

    if (score == -1) {
        resultDiv.innerText = 'You Lose'
    } else if ( score == 0) {
        resultDiv.innerText = 'No one won'
    } else {
        resultDiv.innerText = 'You Won'
    }

    const handsDiv = document.getElementById('hands')
    handsDiv.innerText = `${playerChoice} vs ${computerChoice}`
}


function onClockRPS(playerChoice) {
    console.log(playerChoice)
    const computerChoice = getComputerChoice()
    const score = getResult(playerChoice, computerChoice)
    totalScore['playerScore'] += score

    showResult(score, playerChoice, computerChoice)
}

function playGame() {
    const rpsButtons = document.querySelectorAll('.rpsButton')
    rpsButtons.forEach(rpsButton => {
        rpsButton.onclick = () => { onClockRPS(rpsButton.value) }
    })
    const endGameButton = document.getElementById('endButton')
    endGameButton.onclick = () => { endGame(totalScore) }
}

function endGame(totalScore) {
    totalScore['playerScore'] = 0
    totalScore['playerScore'] = 0

    const resultDiv = document.getElementById('result')

    const handsDiv = document.getElementById('hands')

    resultDiv.innerText = ''

    handsDiv.innerText = ''
}

playGame()