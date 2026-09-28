# Home-page banner photos

This file is not displayed as a page.

One @photo per image. Every page load picks one at random. The first entry is
also the fallback for visitors without JavaScript. 

Fields:
  src    path relative to site/, e.g. assets/images/hero/field-maui.jpg
  alt    short description for screen readers and broken images
  ratio  banner shape as width/height. 3/1 is a wide strip (default),
         2/1 is taller, 16/9 taller still. Photos with different ratios give
         banners of different heights.
  focus  which point of the photo stays visible when cropped, as
         "horizontal vertical" percentages. 50% 50% is the centre (default);
         50% 25% keeps the upper part; 30% 50% keeps the left.

@photo{
  src={assets/images/DSC02274_1.JPG},
  alt={The Kim Lab},
  ratio={3/1},
  focus={50% 40%}
}
