---
title: Kit build guide
---

# Build

Welcome to the build guide for Neptune's DIY kit. We hope you have a great time putting this module together and a wonderful time using it.

Please **read all instructions** thoroughly before starting. If you have questions or run into trouble please reach out to us on [discord] or drop us [an email][email].

This is a **beginner level** kit. Some soldering experience is helpful but not required, though we recommend practicing on another project first. We also have some slightly easier kits available, such as our [Helium kit]. Even if you've got some experience, we recommend taking a look at [Adafruit's guide to excellent soldering][adafruit soldering guide].

This build takes around **one hour** to complete.

[TOC]

[discord]: https://discord.gg/UpfqghQ
[email]: mailto:support@winterbloom.com
[Helium kit]: https://winterbloom.com/shop/helium-kit
[adafruit soldering guide]: https://learn.adafruit.com/adafruit-guide-excellent-soldering


## Tools required

Before you begin, make sure that you've got:

-   Safety glasses. Yes, **really**. A pair like [these][safety glasses] are fine.
-   Proper ventilation, like this [small filtered fan](https://a.co/d/eUfPCRO).
-   A **temperature-controlled** soldering iron, like this [Hakko] or the [Pinecil]. It is very important to use a temperature-controlled iron, since unregulated irons can easily get hot enough to damage components. You should set your iron temperature based on your solder manufacturer's recommendations.
-   Solder. We recommend [Adafruit's SAC305 solder][adafruit solder] or [Kester 275 K100LD].
-   A small flat head screwdriver, like [this one][small screwdriver].

!!! question "Flux"
    We suggest using solder with "no clean" flux. If you use a different kind of flux, be sure to carefully clean the flux residue off based on the guidelines provided by the manufacturer of your solder. Take special care with the LEDs and potentiometers, as they can be damaged by water and flux cleaners.

[safety glasses]: https://a.co/d/dMXvPP6
[tweezers]: https://www.adafruit.com/product/422
[Hakko]: https://www.adafruit.com/product/1204
[Pinecil]: https://pine64.com/product/pinecil-smart-mini-portable-soldering-iron/
[adafruit solder]: https://www.adafruit.com/product/734
[Kester 275 K100LD]: https://www.kester.com/products/product/275-flux-cored-wire
[flux pen]: https://www.sra-solder.com/sra-312-no-clean-flux-pen-refillable
[small screwdriver]: https://lovemyswitches.com/2mm-flat-head-screwdriver-for-knob-set-screws/

## Kit contents

Your kit should contain the following items. If any are missing please [email us][email].

<winter-image-map src="../images/kit/kit-contents.svg">
    <winter-image-map-item id="mainboard">Mainboard</winter-image-map-item>
    <winter-image-map-item id="faceplate">Faceplate</winter-image-map-item>
    <winter-image-map-item id="jacks">1/8" jacks (8)</winter-image-map-item>
    <winter-image-map-item id="jack-nuts">Hex nuts for the 1/8" jacks (8)</winter-image-map-item>
    <winter-image-map-item id="power-header">Eurorack power header</winter-image-map-item>
    <winter-image-map-item id="rubber-bands">Rubber bands (2)</winter-image-map-item>
    <winter-image-map-item id="big-knob">Big knob</winter-image-map-item>
    <winter-image-map-item id="small-knob">Small knobs (3)</winter-image-map-item>
    <winter-image-map-item id="trimpots">Tall trimmer pots (3)</winter-image-map-item>
    <winter-image-map-item id="pots">9mm pots (4)</winter-image-map-item>
    <winter-image-map-item id="pot-washers">Washers for 9mm pots (4)</winter-image-map-item>
    <winter-image-map-item id="pot-nuts">Nuts for 9mm pots (4)</winter-image-map-item>
</winter-image-map>

- (1) Mainboard
- (1) Faceplate
- (8) 1/8" jacks
- (8) Hex nuts for the 1/8" jacks
- (3) Tall trimmer pots
- (4) 9mm pots
- (4) Washers & nuts for the 9mm pots
- (3) Small knobs
- (1) Large knob
- (1) Eurorack power header
- (2) Rubber bands

!!! fairy "Pot washers?"
    We typically screw the 9mm pot's washer and nut onto the shaft when packing kits so they don't get lost. You should remove them before you start the build!

## Power header

Your first task is to solder the 10-pin Eurorack power connector to the mainboard.

![Power header and mainboard](images/kit/1-header-1.webp)

The power connector goes on the **back** side of the board. When placing **note the notch in the outline on the board**. You'll need to make sure the **slot on the connector matches where the notch is on the outline**. The holes for the power connector are designed to be a tight fit, so make sure to push the header firmly flush against the board.

<winter-carousel>
  <img src="../images/kit/1-header-2.webp">
  <img src="../images/kit/1-header-3.webp">
  <img src="../images/kit/1-header-4.webp">
  <img src="../images/kit/1-header-5.webp">
</winter-carousel>

Once placed, make sure to push it flush against the board and then solder the 10 pins on the front side of the board.

<winter-carousel>
  <img src="../images/kit/1-header-5.webp">
  <img src="../images/kit/1-header-6.webp">
  <img src="../images/kit/1-header-7.webp">
  <img src="../images/kit/1-header-8.webp">
</winter-carousel>

!!! warning "Watch out for those LEDs!"
    Avoid touching the LEDs with your iron- they really don't like being melted and they're very hard to replace.


## Pots and jacks

Your next task is to put all of the jacks and pots into place. **Don't solder these yet**, as you'll use the faceplate to help you get everything aligned in the next step.

!!! fairy "Stuffing"
    Fun fact, we call this process "stuffing"! It makes us think of Thanksgiving. 🦃

Start with the four `9mm pots`. Place them onto upper area of mainboard in the spots labeled `cutoff`, `reso`, `salt`, and `fm1`. You may need to bend or straighten the mounting legs on the pots to get them in place.

<winter-carousel>
  <img src="../images/kit/2-pots-1.webp">
  <img src="../images/kit/2-pots-2.webp">
  <img src="../images/kit/2-pots-3.webp">
  <img src="../images/kit/2-pots-4.webp">
  <img src="../images/kit/2-pots-5.webp">
  <img src="../images/kit/2-pots-6.webp">
</winter-carousel>

Next up is the 3 `Tall trimmer pots`. Place these into the three spots in the middle of the mainboard labeled `lp vol`, `hp vol`, and `fm2`.

<winter-carousel>
  <img src="../images/kit/3-trimpots-1.webp">
  <img src="../images/kit/3-trimpots-2.webp">
  <img src="../images/kit/3-trimpots-3.webp">
  <img src="../images/kit/3-trimpots-4.webp">
  <img src="../images/kit/4-all-pots.webp">
</winter-carousel>

Finally, the `1/8" jacks`. These go on the lower area of the mainboard in the spots labeled `reso in`, `salt in`, `fm1 in`, `fm2 in`, `lp in`, `hp in`, `vol in`, and `out`.

<winter-carousel>
  <img src="../images/kit/5-jacks-1.webp">
  <img src="../images/kit/5-jacks-2.webp">
  <img src="../images/kit/5-jacks-3.webp">
  <img src="../images/kit/5-jacks-4.webp">
  <img src="../images/kit/5-jacks-5.webp">
</winter-carousel>

At this point you should have all the jacks and pots in place:

![All things stuffed](./images/kit/6-all-jacks-and-pots.webp)

## Faceplate alignment

Before you get down to soldering, your next task is to use the faceplate to make sure everything is aligned and hold it all in place while you work. Grab the `faceplate` and the two `rubber bands` and then carefully place the faceplate over the jacks and pots.

<winter-carousel>
  <img src="../images/kit/7-jig-1.webp">
  <img src="../images/kit/7-jig-2.webp">
  <img src="../images/kit/7-jig-3.webp">
  <img src="../images/kit/7-jig-4.webp">
</winter-carousel>

Take a moment to check that everything is aligned and flush, as it's much easier to fix now than later! Take the first `rubber band` and wrap it *twice* around the upper part of the module. Try to keep it in the same spot as the picture, since it'll make your life a little easier in the next step.

<winter-carousel>
  <img src="../images/kit/7-jig-5.webp">
  <img src="../images/kit/7-jig-6.webp">
</winter-carousel>

Now take the second `rubber band` and wrap it *twice* around the lower part of the module, once again, try to keep it in the same spot shown.

<winter-carousel>
  <img src="../images/kit/7-jig-7.webp">
  <img src="../images/kit/7-jig-8.webp">
</winter-carousel>

Now that everything is held in place, flip the module over. Double check that all the components are aligned, flush, and that the pins are sticking through all the gold pads.

![Rubber banded](./images/kit/7-jig-9.webp)

## First soldering pass

Now's the time to break out the soldering iron! Your next task is to solder the pots and jacks in place. While you can do all of the soldering in one pass, we recommend following this two pass approach since it gives you one last chance to double check everything before it becomes **much** harder to fix.

!!! warning "Look out below!"
    Be careful when soldering near Neptune's little surface mount components. Keep a close eye on your iron, as it's easy to accidentally angle it in a way that unintentionally hits one of the components.

Start by soldering just the **large, oval** pads for all of the pots:

<winter-carousel>
  <img src="../images/kit/8-tacking-pots-1.webp">
  <img src="../images/kit/8-tacking-pots-2.webp">
  <img src="../images/kit/8-tacking-pots-3.webp">
  <img src="../images/kit/8-tacking-pots-4.webp">
  <img src="../images/kit/8-tacking-pots-5.webp">
  <img src="../images/kit/8-tacking-pots-6.webp">
</winter-carousel>

Next, solder all the pins for the jacks that aren't obscured by the rubber band. You'll come back for the rest later.

<winter-carousel>
  <img src="../images/kit/9-tacking-jacks-1.webp">
  <img src="../images/kit/9-tacking-jacks-2.webp">
  <img src="../images/kit/9-tacking-jacks-3.webp">
  <img src="../images/kit/9-tacking-jacks-4.webp">
  <img src="../images/kit/9-tacking-jacks-5.webp">
  <img src="../images/kit/9-tacking-jacks-6.webp">
</winter-carousel>

Once done, your board should look like the image below:

![Rubber banded](./images/kit/10-tacking-done.webp)

**Take this last chance to double-check your work**. If any of the jacks or pots aren't flush or if any of their little pins managed to bend and miss their holes, fix that now. Once you've completely soldered everything it'll be **much** harder to fix!

## Second soldering pass

With everything in place, you can remove the rubber bands and finish up soldering. Start by taking off the rubber bands and removing the faceplate:

<winter-carousel>
  <img src="../images/kit/11-remove-bands-1.webp">
  <img src="../images/kit/11-remove-bands-2.webp">
</winter-carousel>

Now you can go through and solder all of the remaining legs on the pots and jacks:

<winter-carousel>
  <img src="../images/kit/12-soldering-1.webp">
  <img src="../images/kit/12-soldering-2.webp">
  <img src="../images/kit/12-soldering-3.webp">
  <img src="../images/kit/12-soldering-4.webp">
</winter-carousel>

Once done, your board should look like the following pictures:

<winter-carousel>
  <img src="../images/kit/13-soldering-5.webp">
  <img src="../images/kit/14-soldering-done.webp">
</winter-carousel>

## Hardware

Your next task is to place the washers and nuts on the pots and jacks.

![Hardware](./images/kit/15-hardware-1.webp)

!!! fairy "Dressing"
    Fun fact, we call this process "dressing"! It's like putting fancy clothes on your module. 🤵‍♀️

Start with the four `washers` for the 9mm pots, placing a single washer on each pot shaft:

<winter-carousel>
  <img src="../images/kit/16-hardware-washers-1.webp">
  <img src="../images/kit/16-hardware-washers-2.webp">
  <img src="../images/kit/16-hardware-washers-3.webp">
  <img src="../images/kit/16-hardware-washers-4.webp">
  <img src="../images/kit/16-hardware-washers-5.webp">
  <img src="../images/kit/16-hardware-washers-6.webp">
</winter-carousel>

Once the washers are in place, place the four larger `pot nuts` onto the pot shafts and hand tighten them.

<winter-carousel>
  <img src="../images/kit/17-hardware-pot-nuts-1.webp">
  <img src="../images/kit/17-hardware-pot-nuts-2.webp">
  <img src="../images/kit/17-hardware-pot-nuts-3.webp">
  <img src="../images/kit/17-hardware-pot-nuts-4.webp">
  <img src="../images/kit/17-hardware-pot-nuts-5.webp">
  <img src="../images/kit/17-hardware-pot-nuts-6.webp">
  <img src="../images/kit/17-hardware-pot-nuts-7.webp">
  <img src="../images/kit/17-hardware-pot-nuts-8.webp">
</winter-carousel>

Finally, place the eight smaller `jack nuts` onto each jack and hand tighten them:

<winter-carousel>
  <img src="../images/kit/18-hardware-jack-nuts-1.webp">
  <img src="../images/kit/18-hardware-jack-nuts-2.webp">
  <img src="../images/kit/18-hardware-jack-nuts-3.webp">
  <img src="../images/kit/18-hardware-jack-nuts-4.webp">
  <img src="../images/kit/18-hardware-jack-nuts-5.webp">
</winter-carousel>

Once done, your module should look like the image below.

![Hardware done](./images/kit/19-hardware-done.webp)

## Knobs

Your final task is to add the four knobs to the 9mm pots.

![Knobs](./images/kit/20-knobs-1.webp)

Start by loosening the set screw on each of the knobs using a small flat head screwdriver.

<winter-carousel>
  <img src="../images/kit/20-knobs-2.webp">
  <img src="../images/kit/20-knobs-3.webp">
</winter-carousel>

Next, turn all of the 9mm pots fully counterclockwise. Place the `large knob` on the top right shaft with the indicator line at the **7 o' clock** position. Tighten the set screw to secure the knob in place.

<winter-carousel>
  <img src="../images/kit/21-knob-set-1.webp">
  <img src="../images/kit/21-knob-set-2.webp">
</winter-carousel>

Do the same for the remaining three `small knobs`.

<winter-carousel>
  <img src="../images/kit/21-knob-set-3.webp">
  <img src="../images/kit/21-knob-set-4.webp">
  <img src="../images/kit/21-knob-set-5.webp">
</winter-carousel>

## Finished

Congrats, you finished building your very own Neptune!

![Completed module](images/kit/22-done.webp)

Don't forget to go check out the [User's Guide](/). We'd love to see your work, feel free to tag us on social media - we're `@wntrblm` on both [Twitter] and [Instagram].

If you have any feedback or ran into any issues, feel free to drop us an email at support@winterbloom.com or file a issue on [GitHub].

[Twitter]: https://twitter.com/wntrblm
[Instagram]: https://instagram.com/wntrblm
[GitHub]: https://github.com/wntrblm/Neptune

