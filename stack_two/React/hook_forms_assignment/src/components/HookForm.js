import React, { useState } from 'react';

const HookForm = (props) => {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    const createUser = (e) => {
        //this prevents the default browser refresh and makes sure our state isn't reset
        e.preventDefault();

        const newUser = {
            firstName: firstName,
            lastName: lastName,
            email: email,
            password: password,
            confirmPassword: confirmPassword
        }
        console.log(firstName, lastName, " just joined!")
    }

    return (
    <div>
        <form onSubmit={createUser}>
            <div>
                <label>First Name:</label>
                <input type = "text" onChange={ (e) => setFirstName(e.target.value) }></input>
            </div>
            <div>
                <label>Last Name:</label>
                <input type = "text" onChange = { (e) => setLastName }></input>
            </div>
            <div>
                <label>Email:</label>
                <input type = "text" onChange = { (e) => setEmail(e.target.value) }></input>
            </div>
            <div>
                <label>Password:</label>
                <input type = "text" onChange = { (e) => setPassword(e.target.value)}></input>
            </div>
            <div>
                <label>Confirm Password:</label>
                <input type = "text" onChange = { (e) => setConfirmPassword(e.target.value) }></input>
            </div>
        </form>
        <div>
            <h1>Your Form Data</h1>
            <h2>First Name: {firstName}</h2>
            <h2>Last Name: {lastName}</h2>
            <h2>Email: {email}</h2>
            <h2>Password: {password}</h2>
            <h2>Confirm Password: {confirmPassword}</h2>
        </div>
    </div>
    );
}
export default HookForm;
