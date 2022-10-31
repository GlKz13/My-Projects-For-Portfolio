const BillInput = document.getElementById('BillTotallInput')
const TipInput = document.getElementById('tipInput')
const NumberOfPeopleDiv = document.getElementById('amount')
const perPersonTotalDiv = document.getElementById('sum')

let numberOfPeople = Number(NumberOfPeopleDiv.innerText)


const BillTotalInputUpdate = () => {
    const bill = Number(BillInput.value)
    console.log(bill)
    const tipPercentage = Number(TipInput.value) / 100
    console.log(tipPercentage)

    let tipAmount = bill * tipPercentage

    let total = tipAmount + bill

    let perPersonTotal = total / numberOfPeople

    console.log({total})
    perPersonTotalDiv.innerText = `$${' ' + perPersonTotal.toFixed(2)}`
}

const increasePeople = () => {
    numberOfPeople += 1
    NumberOfPeopleDiv.innerText = numberOfPeople
    BillTotalInputUpdate()
}

const decreasePeople = () => {
    if (numberOfPeople == 1 ) {
        return
    }
    numberOfPeople -= 1
    NumberOfPeopleDiv.innerText = numberOfPeople
    BillTotalInputUpdate()

}