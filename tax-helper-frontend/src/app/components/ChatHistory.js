import { AttachFile, Send } from "@mui/icons-material";
import { Box, Card, FormControl, Grid, IconButton, InputAdornment, OutlinedInput, Typography } from "@mui/material";

export default function Login() {
    return (
        <Box sx={{ 
            minHeight: '100vh',
            minWidth: '100vh',
            justifyContent: 'center',
            alignItems: 'center',
            display: 'flex',
        }}>
            <Card sx={{ 
                width: '100vh', height: '90vh', color: 'primary', borderRadius: 5
            }}>
                <Grid container sx={{ height: '100%'}}>
                    <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', m: 5 }}>
                        <Typography variant="h5">Tax Helper Chat</Typography>
                    </Grid>
                    <Grid item xs={12} sx={{ width: 600, height: 600, overflow: 'auto'}}>
                        {[1, 2, 3, 4].map((value, index) => (
                            <Box key={index} sx={{ml: 5, mr: 5, mt: 4}}>
                                <Typography sx={{m: 1}} variant="body1">{`User ${value % 2 + 1}`}</Typography>
                                <Grid 
                                    item xs={12} 
                                    sx={{ 
                                        p: 2, backgroundColor: 'background.paper', borderRadius: 2,
                                    }}
                                >
                                
                                    <Typography variant="body1">
                                        Can you let me know what I just did? Can you let me know what I just did?
                                        {/* Can you let me know what I just did? Can you let me know what I just did?
                                        Can you let me know what I just did?Can you let me know what I just did?
                                        Can you let me know what I just did? */}
                                    </Typography>
                                </Grid>
                            </Box>
                        ))}
                    </Grid>
                    <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', m: 5 }}>
                        <FormControl  fullWidth variant="outlined">
                            <OutlinedInput
                                id="password"
                                sx={{ height: 80, borderRadius: 5 }}
                                startAdornment={
                                    <InputAdornment position="start">
                                        <AttachFile />
                                    </InputAdornment>
                                }
                                endAdornment={
                                    <InputAdornment position="end">
                                        <IconButton
                                            aria-label="toggle password visibility"
                                            edge="end"
                                        >
                                        <Send />
                                        </IconButton>
                                    </InputAdornment>
                                }
                            />
                        </FormControl>
                    </Grid>
                </Grid>
            </Card>
        </Box>
    );
}