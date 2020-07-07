## Neural Style Transfer


- Optimization technique used to take three images, a content image, a style reference image (such as an artwork by a famous painter).
- The input image which you want to style and blend them together is transformed to look like the content image but “painted” in the style image.

Fine Tune VGG19 model to extract from style image (color featuer only) and content image(all featuers with out color).
then generate new image and merged two image with together(style and content).
