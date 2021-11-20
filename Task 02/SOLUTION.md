hari@HARi:~$ cd /mnt/d             -->To change the working directory
hari@HARi:/mnt/d$ mkdir Coordinates-Location            -->To create a directory                                           
hari@HARi:/mnt/d$ cd Coordinates-Location               
hari@HARi:/mnt/d/Coordinates-Location$ mkdir North          
hari@HARi:/mnt/d/Coordinates-Location$ cd North                                                                                                               
hari@HARi:/mnt/d/Coordinates-Location/North$ touch NDegree.txt          -->To create a file                                                                         
hari@HARi:/mnt/d/Coordinates-Location/North$ echo "9°">NDegree.txt      -->To store a value in the file                                                                                    
hari@HARi:/mnt/d/Coordinates-Location/North$ touch NMinutes.txt                                                                                            
hari@HARi:/mnt/d/Coordinates-Location/North$ echo "5'">NMinutes.txt                                                                                    
hari@HARi:/mnt/d/Coordinates-Location/North$ touch NSeconds.txt                                                                                            
hari@HARi:/mnt/d/Coordinates-Location/North$ echo "38.1\"">NSeconds.txt                                                                                  
hari@HARi:/mnt/d/Coordinates-Location/North$ touch NorthCoordinate.txt                                                                                       
hari@HARi:/mnt/d/Coordinates-Location/North$ cat NDegree.txt NMinutes.txt NSeconds.txt>NorthCoordinate.txt   --> To view the contents                                             
hari@HARi:/mnt/d/Coordinates-Location/North$ mv NorthCoordinate.txt /mnt/d/Coordinates-Location/North.txt                                                      
hari@HARi:/mnt/d/Coordinates-Location/North$ cd /mnt/d/Coordinates-Location                                                                                    
hari@HARi:/mnt/d/Coordinates-Location$ mkdir East                                                                                                             
hari@HARi:/mnt/d/Coordinates-Location$ cd East                                                                                                                
hari@HARi:/mnt/d/Coordinates-Location/East$ touch EDegree.txt                                                                                                  
hari@HARi:/mnt/d/Coordinates-Location/East$ echo "76°">EDegree.txt                                                                                             
hari@HARi:/mnt/d/Coordinates-Location/East$ touch EMinutes.txt                                                                                              
hari@HARi:/mnt/d/Coordinates-Location/East$ echo "29'">EMinutes.txt                                                                                          
hari@HARi:/mnt/d/Coordinates-Location/East$ touch ESeconds.txt                                                                                            
hari@HARi:/mnt/d/Coordinates-Location/East$ echo "30.8\"">ESeconds.txt                                                                               
hari@HARi:/mnt/d/Coordinates-Location/East$ touch EastCoordinate.txt                                                                                  
hari@HARi:/mnt/d/Coordinates-Location/East$ cat EDegree.txt EMinutes.txt ESeconds.txt>EastCoordinate.txt                                             
hari@HARi:/mnt/d/Coordinates-Location/East$ mv EastCoordinate.txt /mnt/d/Coordinates-Location/East.txt                                                
hari@HARi:/mnt/d/Coordinates-Location/East$ cd /mnt/d/Coordinates-Location                                                                               
hari@HARi:/mnt/d/Coordinates-Location$ cat East.txt North.txt>Location-Coordinate.txt                                                                      
hari@HARi:/mnt/d/Coordinates-Location$ touch SOLUTION.md   