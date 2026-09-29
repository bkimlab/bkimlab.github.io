# Banner photos

This file is not displayed as a page.

One @photo per image. A page shows a set with `@hero{set=name}` and every
page load picks one photo of that set at random. The first photo of each set
is also the fallback for visitors without JavaScript.

Files here are the web copies in assets/images/, generated from the originals
in photos/ by `python3 scripts/make_images.py` (lab_theme -> hero/,
group_photos -> group/). Re-run it after adding photos, then add an entry.

Fields:
  set    home (top of the home page), group (top of Members), or
         people/<folder> (rotating profile photo for the @member whose photo=
         lives in that folder; that photo= stays the no-JavaScript fallback)
  src    path relative to site/
  alt    short description for screen readers and broken images
  ratio  banner shape as width/height. All photos in a set share one ratio so
         page height does not depend on which photo loads (5/2 everywhere)
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
  alt={Lab album photo}, ratio={5/2}, focus={50% 60%} }

@photo{ set={group}, src={assets/images/group/20251008-154847.jpg},
  alt={Field collecting selfie}, ratio={5/2}, focus={50% 20%} }

@photo{ set={group}, src={assets/images/group/dsc01397.jpg},
  alt={The lab on coastal rocks}, ratio={5/2}, focus={50% 22%} }

@photo{ set={group}, src={assets/images/group/dsc01443.jpg},
  alt={Examining a vial in the field}, ratio={5/2}, focus={50% 30%} }

@photo{ set={group}, src={assets/images/group/dsc01544.jpg},
  alt={Sorting flies under a field microscope}, ratio={5/2}, focus={50% 40%} }

@photo{ set={group}, src={assets/images/group/dsc02278.jpg},
  alt={The lab at the bench}, ratio={5/2}, focus={50% 28%} }

@photo{ set={group}, src={assets/images/group/dsc02299.jpg},
  alt={The lab with Ally}, ratio={5/2}, focus={50% 45%} }

## People (profile photo pools; box is 120x150, so faces must read at that size)

@photo{ set={people/santosrampasso_augusto}, src={assets/images/people/santosrampasso_augusto/dsc01661.jpg}, focus={50% 25%} }
@photo{ set={people/santosrampasso_augusto}, src={assets/images/people/santosrampasso_augusto/dsc01852.jpg}, focus={70% 25%} }
@photo{ set={people/santosrampasso_augusto}, src={assets/images/people/santosrampasso_augusto/20260307-132851.jpg}, focus={70% 20%} }
@photo{ set={people/santosrampasso_augusto}, src={assets/images/people/santosrampasso_augusto/dsc01348-2.jpg}, focus={50% 45%} }
@photo{ set={people/santosrampasso_augusto}, src={assets/images/people/santosrampasso_augusto/dsc01548-2.jpg}, focus={50% 30%} }
@photo{ set={people/santosrampasso_augusto}, src={assets/images/people/santosrampasso_augusto/dsc01840.jpg}, focus={15% 50%} }

@photo{ set={people/berardi_skyler}, src={assets/images/people/berardi_skyler/dsc01320-2.jpg}, focus={35% 20%} }
@photo{ set={people/berardi_skyler}, src={assets/images/people/berardi_skyler/dsc01303-2.jpg}, focus={42% 38%} }
@photo{ set={people/berardi_skyler}, src={assets/images/people/berardi_skyler/dsc01242.jpg}, focus={55% 35%} }

@photo{ set={people/wang_jocelyn}, src={assets/images/people/wang_jocelyn/dsc01890.jpg}, focus={68% 45%} }
@photo{ set={people/wang_jocelyn}, src={assets/images/people/wang_jocelyn/dsc01186-2.jpg}, focus={50% 30%} }
@photo{ set={people/wang_jocelyn}, src={assets/images/people/wang_jocelyn/dsc01324-2.jpg}, focus={50% 40%} }
@photo{ set={people/wang_jocelyn}, src={assets/images/people/wang_jocelyn/dsc01970.jpg}, focus={25% 30%} }
