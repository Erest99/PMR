HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 1hmm0/hmmdefs -M 1hmm1 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 1hmm1/hmmdefs -M 1hmm2 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 1hmm2/hmmdefs -M 1hmm3 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 1hmm3/hmmdefs -M 1hmm4 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 1hmm4/hmmdefs -M 1hmm5 models0
HERest -C TrainConfig-MFCC39 -I train.mlf -t 250.0 150.0 1000.0 -S train.scp -H 1hmm5/hmmdefs -M 1hmm6 models0
set /p DUMMY=Hit ENTER to continue...