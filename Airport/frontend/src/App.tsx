import React, { useState } from 'react';
import './App.css';
import Card from './components/Card';
import InputField from './components/InputField';
import Button from './components/Button';

const SignIn: React.FC = () => {
  const [email, setEmail] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  
  const handleSignIn = () => {
    console.log('Email:', email, 'Password:', password);
  };

  return (
    <>
    <h1>AIRPORT 3.0</h1>
    <div className="app">
      <Card title="Login">
        <InputField 
          label="Email" 
          type="email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
        />
        <InputField 
          label="Password" 
          type="password" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
        />
        <Button onClick={handleSignIn} text="Sign In" />
      </Card>
    </div>
    </>
  );
};

export default SignIn;