HHEd -H 16hmm6\hmmdefs -M 32hmm0 com32mix models0 
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm0/hmmdefs -M 32hmm1 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm1/hmmdefs -M 32hmm2 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm2/hmmdefs -M 32hmm3 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm3/hmmdefs -M 32hmm4 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm4/hmmdefs -M 32hmm5 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm5/hmmdefs -M 32hmm6 models0
set /p DUMMY=Hit ENTER to continue...