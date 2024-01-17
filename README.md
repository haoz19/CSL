# CSL: Class-Agnostic Structure-Constrained Learning for Segmentation Including the Unseen (AAAI 2024)

[Hao Zhang](https://haoz19.github.io/), Fang Li, [Lu Qi](http://luqi.info/), [Ming-Hsuan Yang](https://faculty.ucmerced.edu/mhyang/), [Narendra Ahuja](https://ece.illinois.edu/about/directory/faculty/n-ahuja)

[[`arXiv`](https://arxiv.org/abs/2312.05538)] 

<div align="center">
  <img src="https://haoz19.github.io/images/csl.png" width="100%" height="100%"/>
</div><br/>

### Features
* A plug-in module for OOD, ZS3 and DA semantic segmentation.
* Rank 1 @ [SMIYC-Anomaly Track & Obstacle Track (w/o OOD) on mean F1](https://segmentmeifyoucan.com/leaderboard)

## Updates
* 2024.1.17 Add raw code.


## Installation (borrow from Mask2Former)

See [installation instructions](INSTALL.md).

## Getting Started

See [Preparing Datasets for CSL](datasets/README.md).

See [Getting Started with CSL](GETTING_STARTED.md).


## Model Zoo


## License

Shield: [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The majority of CSL is licensed under a [MIT License](LICENSE).

However portions of the project are available under separate license terms: Swin-Transformer-Semantic-Segmentation is licensed under the [MIT license](https://github.com/SwinTransformer/Swin-Transformer-Semantic-Segmentation/blob/main/LICENSE), Deformable-DETR is licensed under the [Apache-2.0 License](https://github.com/fundamentalvision/Deformable-DETR/blob/main/LICENSE).

## <a name="CitingCSL"></a>Citing CSL

If you find the code useful, please also consider the following BibTeX entry.

```BibTeX
@misc{zhang2023csl,
      title={CSL: Class-Agnostic Structure-Constrained Learning for Segmentation Including the Unseen}, 
      author={Hao Zhang and Fang Li and Lu Qi and Ming-Hsuan Yang and Narendra Ahuja},
      year={2023},
      eprint={2312.05538},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Acknowledgement

Code is largely based on MaskFormer (https://github.com/facebookresearch/MaskFormer).
