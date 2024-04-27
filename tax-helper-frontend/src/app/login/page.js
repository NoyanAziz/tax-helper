'use client';
import { Visibility, VisibilityOff } from "@mui/icons-material";
import {
    Box, Button, Card, FormControl, Grid, IconButton, InputAdornment, InputLabel, OutlinedInput, TextField, Typography 
} from "@mui/material";
import { useState } from "react";

import { useRouter } from 'next/navigation'



export default function Login() {
    const router = useRouter();

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const handleMouseDownPassword = (event) => {
        event.preventDefault();
    };
    
    return (
    <Box sx={{ 
        minHeight: '100vh',
        justifyContent: 'center',
        alignItems: 'center',
        display: 'flex',
    }}>
        <Card sx={{ 
            width: 450, height: 600, color: 'primary'
        }}>
            <Grid container>
                <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 5 }}>
                    <Typography variant="h5">login</Typography>
                </Grid>
                <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 10}}>
                    <TextField
                        fullWidth
                        sx={{ m: 2}}
                        id="email"
                        label="Email"
                        value={email}
                        type="email"
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </Grid>
                <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', }}>
                    <FormControl fullWidth sx={{ m: 2 }} variant="outlined">
                        <InputLabel htmlFor="password">Password</InputLabel>
                        <OutlinedInput
                            id="password"
                            type={showPassword ? 'text' : 'password'}
                            endAdornment={
                            <InputAdornment position="end">
                                <IconButton
                                    aria-label="toggle password visibility"
                                    onClick={() => setShowPassword(!showPassword)}
                                    onMouseDown={handleMouseDownPassword}
                                    edge="end"
                                >
                                {showPassword ? <VisibilityOff /> : <Visibility />}
                                </IconButton>
                            </InputAdornment>
                            }
                            label="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </FormControl>
                </Grid>
                <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', mt: 10}}>
                    <Button
                        fullWidth
                        sx={{ height: 50, m: 2}}
                        variant="outlined"
                        type="submit"
                        onClick={() => {
                            console.log()
                            router.push('/');
                        }}
                    >
                        <Typography variant="button">login</Typography>
                    </Button>
                </Grid>
            </Grid>
        </Card>
       </Box>
    );
}