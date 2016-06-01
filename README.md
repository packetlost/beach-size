# beach-size

**Because this script performs many factorials (and is poorly optimized), please consider your CPU before inputting large values**

This is a quick-and-dirty script to describe the difficulty of locating a file on a distributed storage network without information regarding the locations of its shards. It computes the probability of locating all the shards of a file with a number of random non-repeating draws from a network containing a given number of shards.

This is a fairly simple application of a [hypergeometric distribution](https://en.wikipedia.org/wiki/Hypergeometric_distribution). The population size (N) is the total number of shards on the network, the number of successes in the population (k) is the number of shards required to rebuild the file, the sample size (n) is the number of shards a searcher retrieves from the network, and the number of success of shards in the file (x) is equal to the number of shards in the file (i.e. all shards are required to rebuild the file).

The results csv is formatted as a series of tables. Each table varies N and n for a constant x. The network size (N) is laid out horizontally, while the sample size (n) is vertical. The cells in the table correspond to ```hypergeo(N,x,n,x)```.  The tables show a clear linear relationship between network size and difficulty of locating a file without prior knowledge.

In this context, security can be thought of as the number of operations required to locate a given shard without prior knowledge. The security of a shard is therefore directly proportional to the size of the network. This indicates that the security of the network is proportional to the square of the network size, implying there is a network effect of security.

This analysis is a little naive. It doesn’t account for redundancy schemes, or consistency schemes involving Reed-Solomon or similar erasure coding across shards. It doesn’t attempt to determine optimal strategies for attackers seeking files on the network. It's a work-in-progress.
