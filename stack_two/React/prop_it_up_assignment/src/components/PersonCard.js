import React from 'react';
const PersonCard = (props) => {
    return (
        <div>
            <h1>{props.firstName}, {props.lastName}</h1>
            <p>Hair Color: {props.hairColor}</p>
            <p>Age: {props.age}</p>
        </div>
    );
}
export default PersonCard; 
