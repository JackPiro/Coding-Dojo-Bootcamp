import React, { useState } from 'react';

const PersonCard = (props) => {
    const [age, setAge] = useState(20);
    return (
        <div>
            <h1>{props.firstName}, {props.lastName}</h1>
            <p>Age: {age}</p>
            <p>hairColor: {props.hairColor}</p>
            <button onClick = { (event) => setAge(age + 1) }>Its {props.firstName}'s B Day!</button>
        </div>
    );
}
export default PersonCard;
