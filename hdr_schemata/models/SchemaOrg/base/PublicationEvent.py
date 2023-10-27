from typing import Optional, Union
from pydantic import AnyUrl, BaseModel, RootModel, Field,  EmailStr

from .Organization import Organization
from .Person import Person
from .Thing import Thing
from hdr_schemata.definitions.SchemaOrg import Text, Number, Date, DateTime


class PublicationEvent(BaseModel):

    m_type: Text = Field(
        alias="@type",
        default="PublicationEvent"
    )
    
    
    publishedBy: Optional[Union[Organization, Person]] = Field(
        None,
        description=r'''An agent associated with the publication event.'''
    )
    
    
    #publishedOn: Optional[BroadcastService] = Field(
    publishedOn: Optional[Text] = Field(
        None,
        description=r'''A broadcast service associated with the publication event.'''
    )


    about: Optional[Thing] = Field(
        None,
        description=r'''The subject matter of the content.
        
        
        Inverse property: 
        subjectOf'''
    )
    
    
    # actor: Optional[Person] = Field(
    #     None,
    #     description=r'''An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
    #     Supersedes 
        
        
        
    #     actors.'''
    # )
    
    
    # aggregateRating: Optional[AggregateRating] = Field(
    #     None,
    #     description=r'''The overall rating, based on a collection of reviews or ratings, of the item.'''
    # )
    
    
    # attendee: Optional[Union[Organization, Person]] = Field(
    #     None,
    #     description=r'''A person or organization attending the event.
    #     Supersedes 
        
        
        
    #     attendees.'''
    # )
    
    
    # audience: Optional[Audience] = Field(
    #     None,
    #     description=r'''An intended audience, i.e. a group for whom something was created.
    #     Supersedes 
        
        
        
    #     serviceAudience.'''
    # )
    
    
    # composer: Optional[Union[Organization, Person]] = Field(
    #     None,
    #     description=r'''The person or organization who wrote a composition, or who is the composer of a work performed at some event.'''
    # )
    
    
    # contributor: Optional[Union[Organization, Person]] = Field(
    #     None,
    #     description=r'''A secondary contributor to the CreativeWork or Event.'''
    # )
    
    
    # director: Optional[Person] = Field(
    #     None,
    #     description=r'''A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
    #     Supersedes 
        
        
        
    #     directors.'''
    # )
    
    
    # doorTime: Optional[Union[DateTime, Time]] = Field(
    #     None,
    #     description=r'''The time admission will commence.'''
    # )
    
    
    # duration: Optional[Duration] = Field(
    #     None,
    #     description=r'''The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.'''
    # )
    
    
    # endDate: Optional[Union[Date, DateTime]] = Field(
    #     None,
    #     description=r'''The end date and time of the item (in ISO 8601 date format).'''
    # )
    
    
    # eventAttendanceMode: Optional[EventAttendanceModeEnumeration] = Field(
    #     None,
    #     description=r'''The eventAttendanceMode of an event indicates whether it occurs online, offline, or a mix.'''
    # )
    
    
    # eventSchedule: Optional[Schedule] = Field(
    #     None,
    #     description=r'''Associates an Event with a Schedule. There are circumstances where it is preferable to share a schedule for a series of
    #     repeating events rather than data on the individual events themselves. For example, a website or application might prefer to publish a schedule for a weekly
    #     gym class rather than provide data on every event. A schedule could be processed by applications to add forthcoming events to a calendar. An Event that
    #     is associated with a Schedule using this property should not have startDate or endDate properties. These are instead defined within the associated
    #     Schedule, this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules, e.g. for different months
    #     or seasons.'''
    # )
    
    
    # eventStatus: Optional[EventStatusType] = Field(
    #     None,
    #     description=r'''An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled.'''
    # )
    
    
    # funder: Optional[Union[Organization, Person]] = Field(
    #     None,
    #     description=r'''A person or organization that supports (sponsors) something through some kind of financial contribution.'''
    # )
    
    
    # funding: Optional[Grant] = Field(
    #     None,
    #     description=r'''A Grant that directly or indirectly provide funding or sponsorship for this item. See also ownershipFundingInfo.
        
        
    #     Inverse property: 
    
        
    #     fundedItem'''
    # )
    
    
    # inLanguage: Optional[Union[Language, Text]] = Field(
    #     None,
    #     description=r'''The language of the content or performance or used in an action. Please use one of the language codes from the IETF BCP 47 standard. See also availableLanguage.
    #     Supersedes 
        
        
        
    #     language.'''
    # )
    
    
    # isAccessibleForFree: Optional[Boolean] = Field(
    #     None,
    #     description=r'''A flag to signal that the item, event, or place is accessible for free.
    #     Supersedes 
        
        
        
    #     free.'''
    # )
    
    
    # keywords: Optional[Union[DefinedTerm, Text, AnyURL]] = Field(
    #     None,
    #     description=r'''Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.'''
    # )
    
    
    # location: Optional[Union[Place, PostalAddress, Text, VirtualLocation]] = Field(
    #     None,
    #     description=r'''The location of, for example, where an event is happening, where an organization is located, or where an action takes place.'''
    # )
    
    
    # maximumAttendeeCapacity: Optional[Integer] = Field(
    #     None,
    #     description=r'''The total number of individuals that may attend an event or venue.'''
    # )
    
    
    # maximumPhysicalAttendeeCapacity: Optional[Integer] = Field(
    #     None,
    #     description=r'''The maximum physical attendee capacity of an Event whose eventAttendanceMode is OfflineEventAttendanceMode (or the offline aspects, in the case of a MixedEventAttendanceMode).'''
    # )
    
    
    # maximumVirtualAttendeeCapacity: Optional[Integer] = Field(
    #     None,
    #     description=r'''The maximum virtual attendee capacity of an Event whose eventAttendanceMode is OnlineEventAttendanceMode (or the online aspects, in the case of a MixedEventAttendanceMode).'''
    # )
    
    
    # offers: Optional[Union[Demand, Offer]] = Field(
    #     None,
    #     description=r'''An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use businessFunction to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a Demand. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        
        
    #     Inverse property: 
        
        
    #     itemOffered'''
    # )
    
    
    # organizer: Optional[Union[Organization, Person]] = Field(
    #     None,
    #     description=r'''An organizer of an Event.'''
    # )
    
    
    # performer: Optional[Union[Organization, Person]] = Field(
    #     None,
    #     description=r'''A performer at the event—for example, a presenter, musician, musical group or actor.
    #     Supersedes 
        
        
        
    #     performers.'''
    # )
    
    
    # previousStartDate: Optional[Date] = Field(
    #     None,
    #     description=r'''Used in conjunction with eventStatus for rescheduled or cancelled events. This property contains the previously scheduled start date. For rescheduled events, the startDate property should be used for the newly scheduled start date. In the (rare) case of an event that has been postponed and rescheduled multiple times, this field may be repeated.'''
    # )
    
    
    # recordedIn: Optional[Union[CreativeW, k]] = Field(
    #     None,
    #     description=r'''The CreativeWork that captured all or part of this Event.
        
        
    #     Inverse property: 
        
    
    #     recordedAt'''
    # )
    
    
    # remainingAttendeeCapacity: Optional[Integer] = Field(
    #     None,
    #     description=r'''The number of attendee places for an event that remain unallocated.'''
    # )
    
    
    # review: Optional[Review] = Field(
    #     None,
    #     description=r'''A review of the item.
    #     Supersedes 
        
        
        
    #     reviews.'''
    # )
    
    
    # sponsor: Optional[Union[Organization, Person]] = Field(
    #     None,
    #     description=r'''A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.'''
    # )
    
    
    startDate: Optional[Union[Date, DateTime]] = Field(
        None,
        description=r'''The start date and time of the item (in ISO 8601 date format).'''
    )
    
    
    # subEvent: Optional[Event] = Field(
    #     None,
    #     description=r'''An Event that is part of this event. For example, a conference event includes many presentations, each of which is a subEvent of the conference.
    #     Supersedes 
        
        
        
    #     subEvents.
        
    #     Inverse property: 
        
        
    #     superEvent'''
    # )
    
    
    # superEvent: Optional[Event] = Field(
    #     None,
    #     description=r'''An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.
        
        
    #     Inverse property: 
        
        
    #     subEvent'''
    # )
    
    
    # translator: Optional[Union[Organization, Person]] = Field(
    #     None,
    #     description=r'''Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.'''
    # )
    
    
    # typicalAgeRange: Optional[Text] = Field(
    #     None,
    #     description=r'''The typical expected age range, e.g. '7-9', '11-'.'''
    # )
    
    
    # workFeatured: Optional[Union[CreativeW, k]] = Field(
    #     None,
    #     description=r'''A work featured in some event, e.g. exhibited in an ExhibitionEvent.
    #     Specific subproperties are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent).'''
    # )
    
    
    # workPerformed: Optional[Union[CreativeW, k]] = Field(
    #     None,
    #     description=r'''A work performed in some event, for example a play performed in a TheaterEvent.'''
    # )
    
    
