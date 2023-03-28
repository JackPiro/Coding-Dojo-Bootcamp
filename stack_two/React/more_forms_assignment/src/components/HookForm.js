import React, { useState } from 'react';

const HookForm = (props) => {
    const [firstName, setFirstName] = useState("");
    // const [firstNameError, setFirstNameError] = useState("");
    const [lastName, setLastName] = useState("");
    // const [lastNameError, setLastNameError] = useState("");
    const [email, setEmail] = useState("");
    // const [emailError, setEmailError] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    // const [passwordMatchError, setPasswordMatchError] = useState("");
    // const [passwordLenError, setPasswordLenError] = useState("");
    
    // const firstNameHandler = (e) => {
    //     setFirstName(e.target.value);
    //     if (e.target.value < 3) {
    //         setFirstNameError("First name Must be more than 2 characters.");
    //     }
    //     else {
    //         setFirstNameError("");
    //     }
    // }

    // const LastNameHandler = (e) => {
    //     setLastName(e.target.value);
    //     if (e.target.value < 3) {
    //         setLastNameError("Last name Must be more than 2 characters.");
    //     }
    //     else {
    //         setLastNameError("");
    //     }
    // }

    // const emailHandler = (e) => {
    //     setEmail(e.target.value);
    //     if (e.target.value < 3) {
    //         setEmailError("Email Must be more than 2 characters.");
    //     }
    //     else {
    //         setEmailError("");
    //     }
    // }

    // const passwordHandler = (e) => {
    //     setPassword(e.target.value);
    //     if (e.target.value < 3) {
    //         setPasswordLenError("Password Must be more than 2 characters.");
    //     }
    //     else {
    //         setPasswordLenError("");
    //     }
    // }


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
                {firstName.length < 2 && firstName.length > 0 ? (<p>First Name must be at least 2 characters</p>) : null}
            </div>
            <div>
                <label>Last Name:</label>
                <input type = "text" onChange = { (e) => setLastName(e.target.value) }></input>
                {lastName.length < 2 && lastName.length > 0 ? (<p>Last Name must be at least 2 characters</p>) : null}
            </div>
            <div>
                <label>Email:</label>
                <input type = "text" onChange = { (e) => setEmail(e.target.value) }></input>
                {email.length < 5 ? <p>Email must be at least 5 characters</p> : null}
            </div>
            <div>
                <label>Password:</label>
                <input type = "text" onChange = { (e) => setPassword(e.target.value)}></input>
                {password.length < 8 ? (<p>Password must be at least 8 characters</p>) : null}
            </div>
            <div>
                <label>Confirm Password:</label>
                <input type = "text" onChange = { (e) => setConfirmPassword(e.target.value) }></input>
                {confirmPassword !== password ? <p>Passwords must match</p> : null}
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
