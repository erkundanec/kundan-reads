# Batch Size
## A complete guide of how to use git and github

## Introduction
The batch size refers to the number of samples passed through the model before optimizing it. The gradient for each sample is either summed or averaged and then used to update the parameters. This process continues for the next batch, and so on. A common question is, "should I use powers of 2 when choosing the size of a batch size when training my Neural Network?"

### View 1:
A large batch size generally leads to poor generalization because, before updating the parameters, the gradients are averaged out. This may cause the network to overlook small details in an image, potentially leading to the model getting stuck in local minima. While a small batch size can overcome this problem, the rate of convergence is slower.

The optimal batch size depends on the dataset and the task. A standard approach is to select a batch size as a power of 2, but there is no hard and fast rule. It depends on GPU memory and may require tuning to find the optimal batch size.

### View 2:
Some researchers argue that there's nothing special about powers of two for batch sizes. The recommendation is to use the maximum batch size that fits into GPU/RAM to fully utilize available resources. The key aspects of batch-wise training are speed and the addition of minibatch noise to SGD. These factors have no direct relation to powers of two for batch size. Image resizing to a power of two makes sense due to common use of 2x2 pooling windows, but that's a different consideration.

### View 3:
Others suggest using powers of 2 when choosing the batch size for training a Neural Network. The reasoning is that CPU and GPU memory architecture often organizes memory in powers of 2 (check page size in your CPU using `getconf PAGESIZE` in Linux). For efficiency reasons, having mini-batch sizes as powers of 2 ensures alignment to page boundaries, potentially speeding up data fetch to memory. Typical values used are 256 or 512, and some practitioners also use 1024. The idea is to fit a chunk (or multiple chunks) into a page, and powers of 2 ensure that alignment happens.

## Epoch vs Batch Size vs Iterations
To understand the difference between these terms, familiarity with some machine learning concepts, such as Gradient Descent, is necessary.
