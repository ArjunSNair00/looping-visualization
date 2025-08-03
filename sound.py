import numpy as np
import sounddevice as sd

def main():
  for i in range(1,10):
    # #white noise
    # mysound = white_noise(0.2,0.01,44100)
    # sd.play(mysound)
    # sd.wait()

    # #kick
    # mysound=sine_tone(50,0.5,0.3,44100)
    # sd.play(mysound)
    # sd.wait()

    #additive synthesis
    sines = [sine_tone(
            frequency=20 + (i+40*2) * j + 600,
            amplitude=0.3 / j,
            duration=0.3
        )for j in range(1, 100, 2)]
    #combine the sines
    mysound=sum(sines)
    sd.play(mysound)
    sd.wait()
    
  
def sine_tone(
    frequency: int=440,
    duration: float=1.0,
    amplitude:float=0.1,
    sample_rate:int=44100)->np.ndarray:
  
  #create the number of samples required
  n_samples=int(sample_rate*duration)

  #create an array of timepoints
  time_points=np.linspace(0,duration,n_samples,False)

  #create the sine wave
  sine=np.sin(2*np.pi*frequency*time_points)

  #apply the amplitude and return the tone
  sine *= amplitude
  return sine

def white_noise(
    duration: float=1.0,
    amplitude:float=0.1,
    sample_rate:int=44100)->np.ndarray:
  
  n_samples=int(duration * sample_rate)
  noise=np.random.uniform(-1,1,n_samples)
  noise*=amplitude
  return noise

main()