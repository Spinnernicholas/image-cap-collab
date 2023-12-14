# image-cap-collab
Collaborative Image Captioning Annotation Tool

## Captions

In this application, captions are used to provide descriptive information about the images. Each caption consists of a text string and a set of tags. Tags can be of two types:

1. **Literal Tags**: These are simple string tags that directly describe some aspect of the image.

2. **Function Tags**: These are more complex tags that consist of a function and an argument. The function describes what aspect of the image the tag refers to, and the argument provides the specific detail. For example, a function tag might be `size_large` to indicate that the image shows a large object.

When a caption is displayed, the tags (sorted in alphabetical order) are concatenated at the beginning of the caption string, separated by commas. For example, a caption might look like this: `apple, banana, cherry, color_red, size_large, A description of the fruit.`

This structure allows for a rich and flexible description of each image, and can easily be extended to include new types of tags or other information.

## Function Tag Argument Data Types

Function tags can have arguments of several basic data types:

1. **Text**: This is a simple string of characters.

2. **Choice**: This is a selection from a predefined set of options.

3. **Integer**: This is a whole number. An optional range restriction can be specified, in which case the number must fall within the specified range.

4. **Decimal**: This is a number that can have a fractional part. Like with integers, an optional range restriction can be specified.

When defining a function tag, you should specify the argument data type and, if applicable, the range or set of options. For example, a function tag might be `size_large` where `size` is the function, `large` is the argument, and the argument data type is `Choice` with options `['small', 'medium', 'large']`.