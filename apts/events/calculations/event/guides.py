def _get_dynamic_event_guide(cat: str, title_lower: str) -> list[str] | None:
    """Evaluates dynamic event category guide rules for satellites, launches, meteors, and alignments."""
    from apts.i18n import gettext_

    if cat in ("FLYBY", "ISS_FLYBY", "TIANGONG_FLYBY") or "flyby" in title_lower or "iss" in title_lower:
        return [
            gettext_("Find an open viewing location with a clear view of the sky in the pass direction."),
            gettext_("Check the exact rise time and direction before heading outside."),
            gettext_("Watch the horizon for a bright, steady, non-blinking point of light moving across the sky."),
            gettext_("Track the satellite visually with naked eye or wide-field binoculars."),
            gettext_("Note the time and peak altitude as it passes overhead."),
        ]
    if cat in ("ROCKET_LAUNCH", "SPACE_LAUNCH") or "launch" in title_lower or "rocket" in title_lower:
        return [
            gettext_("Confirm the launch schedule and trajectory azimuth prior to liftoff."),
            gettext_("Find an elevated or unobstructed location facing the launch direction."),
            gettext_("Look low near the horizon at T+2 to T+3 minutes for the rising exhaust plume."),
            gettext_("Use binoculars to spot stage separation or twilight expansion effects."),
        ]
    if cat == "METEOR_SHOWER" or "shower" in title_lower or "meteor" in title_lower:
        return [
            gettext_("Choose a dark location away from city lights."),
            gettext_("Allow 20–30 minutes for your eyes to fully adapt to darkness."),
            gettext_("Lie back comfortably on a reclining chair facing the radiant direction."),
            gettext_("Observe with the naked eye for the widest field of view."),
            gettext_("Keep warm and count the number of meteors per hour."),
        ]
    if cat in ("PLANET_ALIGNMENT", "CELESTIAL_CONFIGURATION") or "alignment" in title_lower:
        return [
            gettext_("Find a site with a clear view spanning East to West along the ecliptic arc."),
            gettext_("Begin observing during early twilight as the brightest planets emerge."),
            gettext_("Scan along the ecliptic line to identify all participating planets."),
            gettext_("Use wide-angle camera gear or binoculars to capture the full parade."),
        ]
    if "jovian" in cat.lower() or "jovian" in title_lower or "grs" in title_lower or "jupiter" in title_lower:
        return [
            gettext_("Set up a telescope with medium-to-high magnification (100x–200x)."),
            gettext_("Allow your optical tube time to thermally stabilize outdoors."),
            gettext_("Locate Jupiter and identify the equatorial dark cloud bands."),
            gettext_("Observe the positions of the four Galilean moons (Io, Europa, Ganymede, Callisto)."),
            gettext_("Look for moon shadow transits or the Great Red Spot during peak visibility."),
        ]
    return None


def get_step_by_step_guide(category: str, title: str = "", objects: list[str] | None = None) -> list[str]:
    """Generates step-by-step observational guide instructions for an event."""
    from apts.i18n import gettext_

    cat = category.upper()
    title_lower = str(title).lower()

    dynamic_guide = _get_dynamic_event_guide(cat, title_lower)
    if dynamic_guide:
        return dynamic_guide

    static_guides: dict[str, list[str]] = {
        "OCCULTATION": [
            gettext_("Verify that the occultation is visible from your location."),
            gettext_("Arrive and set up equipment at least 15–30 minutes before the event."),
            gettext_("Focus carefully before the occultation begins."),
            gettext_("Watch continuously near the predicted disappearance time."),
            gettext_("If possible, record the event with a camera or video setup."),
        ],
        "CONJUNCTION": [
            gettext_("Find an observing location with an unobstructed horizon in the specified direction."),
            gettext_("Set up binoculars or a telescope 15–20 minutes before peak alignment."),
            gettext_("Locate the brighter object first, then scan near it to find the companion."),
            gettext_("Observe both objects together within the same field of view."),
            gettext_("Capture wide-field photographs during twilight or dark sky hours."),
        ],
        "SOLAR_ECLIPSE": [
            gettext_("Ensure you have ISO-certified solar viewing glasses or solar filters."),
            gettext_("Inspect all solar filters for damage before looking at the Sun."),
            gettext_("Set up your viewing area in advance with a clear line of sight."),
            gettext_("Observe the progression of solar coverage safely."),
            gettext_("Never look directly at the Sun without approved solar filtration."),
        ],
        "LUNAR_ECLIPSE": [
            gettext_("Find a comfortable viewing spot with a clear view of the Moon."),
            gettext_("No special eye protection is needed; binoculars or small telescopes enhance the view."),
            gettext_("Observe the gradual darkening and copper-red color shift during totality."),
            gettext_("Take long-exposure photographs as the Moon passes through Earth's umbra."),
        ],
        "OPPOSITION": [
            gettext_("Plan your observation around midnight when the planet reaches its highest altitude."),
            gettext_("Use a telescope with moderate to high magnification for fine surface details."),
            gettext_("Allow your telescope to thermally acclimate to outdoor temperatures."),
            gettext_("Observe during periods of steady atmospheric seeing."),
        ],
        "TRANSIT": [
            gettext_("Equip your optical setup with safe, dedicated solar filters."),
            gettext_("Track the ingress and egress times of the transit carefully."),
            gettext_("Use high magnification to resolve the silhouette against the solar disk."),
            gettext_("Record timestamped images throughout the transit progression."),
        ],
    }

    if cat in static_guides:
        return static_guides[cat]

    if cat in ("GREATEST_ELONGATION", "VENUS_GREAT_BRILLIANCY"):
        return [
            gettext_("Locate the planet low near the horizon in early morning or evening twilight."),
            gettext_("Use binoculars or a small telescope to observe its crescent or gibbous phase."),
            gettext_("Observe before sunrise or after sunset when contrast is optimal."),
        ]

    if cat in ("MOON_PHASE", "SUPERMOON", "MOON_LIBRATION", "LUNAR_FEATURE"):
        return [
            gettext_("Choose a viewing spot with clear sky access toward the Moon."),
            gettext_("Use binoculars or a telescope along the lunar terminator line for shadow details."),
            gettext_("Observe prominent craters, mountain ranges, and maria surface features."),
        ]

    obj_str = " or ".join([gettext_(o) for o in objects]) if objects else gettext_("target")
    return [
        gettext_("Check local weather and cloud cover prior to the event."),
        gettext_("Locate {target} in the sky using cardinal directions and altitude.").format(target=obj_str),
        gettext_("Use appropriate optical aid (naked eye, binoculars, or telescope)."),
        gettext_("Observe near the predicted peak viewing time for the best view."),
    ]


def build_event_description(
    category: str,
    title: str,
    objects: list[str],
    datetime_utc_str: str,
    location_name: str,
    angular_separation: str | None = None,
) -> str:
    """Generates a narrative description for the event."""
    from apts.i18n import gettext_

    sep_text = f" {gettext_('with an angular separation of')} {angular_separation}" if angular_separation else ""
    o1 = gettext_(objects[0]) if len(objects) >= 1 else gettext_("Target")
    o2 = gettext_(objects[1]) if len(objects) >= 2 else gettext_("Companion")
    loc = gettext_(location_name)

    if category == "OCCULTATION" and len(objects) >= 2:
        return gettext_("The {object1} will pass directly in front of {object2}, creating a lunar occultation visible from {location} at {time}.").format(
            object1=o1, object2=o2, location=loc, time=datetime_utc_str
        )
    elif category == "CONJUNCTION" and len(objects) >= 2:
        return gettext_("{object1} and {object2} will share a close celestial conjunction{separation}, visible in the sky from {location}.").format(
            object1=o1, object2=o2, separation=sep_text, location=loc
        )
    elif category == "METEOR_SHOWER":
        shower_name = o1 if objects else title
        return gettext_("Peak activity for the {shower} meteor shower, offering optimal viewing conditions from {location}.").format(
            shower=shower_name, location=loc
        )
    else:
        return gettext_("{title} occurring on {time}, visible from {location}.").format(
            title=title, time=datetime_utc_str, location=loc
        )
