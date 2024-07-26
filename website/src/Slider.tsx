import * as React from 'react';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';


export default function ContinuousSlider() {
    const [value, setValue] = React.useState<number>(30);

    const handleChange = (event: Event, newValue: number | number[]) => {
        setValue(newValue as number);
    };

    return (
        <Box >
            <Stack spacing={3} direction="row" alignItems="center">
                <Typography sx={{ mb: 5 }} id="continuous-slider">
                    Mood: {value}
                </Typography>
                <Slider aria-label="Volume" value={value} onChange={handleChange} />
            </Stack>
            {/* <Slider disabled defaultValue={30} aria-label="Disabled slider" /> */}
        </Box>
    );
}