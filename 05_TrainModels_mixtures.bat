HHEd -H 1hmm6\hmmdefs -M 2hmm0 com2mix models0 
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 2hmm0/hmmdefs -M 2hmm1 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 2hmm1/hmmdefs -M 2hmm2 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 2hmm2/hmmdefs -M 2hmm3 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 2hmm3/hmmdefs -M 2hmm4 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 2hmm4/hmmdefs -M 2hmm5 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 2hmm5/hmmdefs -M 2hmm6 models0

HHEd -H 2hmm6\hmmdefs -M 4hmm0 com4mix models0 
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 4hmm0/hmmdefs -M 4hmm1 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 4hmm1/hmmdefs -M 4hmm2 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 4hmm2/hmmdefs -M 4hmm3 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 4hmm3/hmmdefs -M 4hmm4 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 4hmm4/hmmdefs -M 4hmm5 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 4hmm5/hmmdefs -M 4hmm6 models0

HHEd -H 4hmm6\hmmdefs -M 8hmm0 com8mix models0 
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 8hmm0/hmmdefs -M 8hmm1 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 8hmm1/hmmdefs -M 8hmm2 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 8hmm2/hmmdefs -M 8hmm3 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 8hmm3/hmmdefs -M 8hmm4 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 8hmm4/hmmdefs -M 8hmm5 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 8hmm5/hmmdefs -M 8hmm6 models0

HHEd -H 8hmm6\hmmdefs -M 16hmm0 com16mix models0 
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 16hmm0/hmmdefs -M 16hmm1 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 16hmm1/hmmdefs -M 16hmm2 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 16hmm2/hmmdefs -M 16hmm3 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 16hmm3/hmmdefs -M 16hmm4 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 16hmm4/hmmdefs -M 16hmm5 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 16hmm5/hmmdefs -M 16hmm6 models0

HHEd -H 16hmm6s\hmmdefs -M 32hmm0 com32mix models0 
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm0/hmmdefs -M 32hmm1 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm1/hmmdefs -M 32hmm2 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm2/hmmdefs -M 32hmm3 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm3/hmmdefs -M 32hmm4 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm4/hmmdefs -M 32hmm5 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 32hmm5/hmmdefs -M 32hmm6 models0
set /p DUMMY=Hit ENTER to continue...