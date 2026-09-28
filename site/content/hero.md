# Banner photos

This file is not displayed as a page.

One @photo per image. A page shows a set with `@hero{set=name}` and every
page load picks one photo of that set at random. The first photo of each set
is also the fallback for visitors without JavaScript.

Files here are the web copies in assets/images/, generated from the originals
in photos/ by `python3 scripts/make_images.py` (lab_theme -> hero/,
group_photos -> group/). Re-run it after adding photos, then add an entry.

Fields:
  set    home (top of the home page) or group (top of Members)
  src    path relative to site/
  alt    short description for screen readers and broken images
  ratio  banner shape as width/height; all banners use 5/2 so page height
         does not depend on which photo loads
  focus  the point of the photo that stays visible when cropped to the
         banner, as "horizontal vertical" percentages (50% 50% = centre,
         50% 35% = keep the upper part). Faces should sit near the focus.

## Home

@photo{ set={home}, src={assets/images/hero/069a3522.jpg},
  alt={A Drosophila on a dry stem}, ratio={5/2}, focus={65% 55%} }

@photo{ set={home}, src={assets/images/hero/069a3529-enhanced.jpg},
  alt={Two Drosophila feeding on fermenting fruit}, ratio={5/2}, focus={50% 45%} }

@photo{ set={home}, src={assets/images/hero/069a4466.jpg},
  alt={A collecting vial of flies held in a hand}, ratio={5/2}, focus={55% 50%} }

@photo{ set={home}, src={assets/images/hero/069a4834-enhanced-nr.jpg},
  alt={Wild-caught flies in a labelled vial}, ratio={5/2}, focus={45% 45%} }

@photo{ set={home}, src={assets/images/hero/069a4957-enhanced-nr.jpg},
  alt={Collecting along a fern-lined canyon stream}, ratio={5/2}, focus={50% 55%} }

@photo{ set={home}, src={assets/images/hero/dsc01134-2.jpg},
  alt={A rack of labelled collecting vials in the field}, ratio={5/2}, focus={45% 60%} }

@photo{ set={home}, src={assets/images/hero/dsc01975.jpg},
  alt={Flies swarming a fallen durian}, ratio={5/2}, focus={50% 50%} }

@photo{ set={home}, src={assets/images/hero/dsc01990.jpg},
  alt={Guyot Hall on a snowy night}, ratio={5/2}, focus={50% 55%} }

## Members

@photo{ set={group}, src={assets/images/group/dsc02274-1.jpg},
  alt={The lab in lab coats}, ratio={5/2}, focus={50% 40%} }

@photo{ set={group}, src={assets/images/group/20251008-154847.jpg},
  alt={Field collecting selfie}, ratio={5/2}, focus={50% 35%} }

@photo{ set={group}, src={assets/images/group/dsc01397.jpg},
  alt={The lab on coastal rocks}, ratio={5/2}, focus={50% 35%} }

@photo{ set={group}, src={assets/images/group/dsc01443.jpg},
  alt={Examining a vial in the field}, ratio={5/2}, focus={50% 30%} }

@photo{ set={group}, src={assets/images/group/dsc01544.jpg},
  alt={Sorting flies under a field microscope}, ratio={5/2}, focus={50% 40%} }

@photo{ set={group}, src={assets/images/group/dsc01664.jpg},
  alt={Lab dinner}, ratio={5/2}, focus={50% 45%} }

@photo{ set={group}, src={assets/images/group/dsc02278.jpg},
  alt={The lab at the bench}, ratio={5/2}, focus={50% 40%} }

@photo{ set={group}, src={assets/images/group/dsc02299.jpg},
  alt={The lab with the Guyot Hall dinosaur}, ratio={5/2}, focus={50% 45%} }
