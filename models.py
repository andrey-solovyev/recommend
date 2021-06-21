import bdb
import json

from __init__ import *


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]


def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)


class Result(db.Model):
    __tablename__ = 'twitt'

    id = db.Column('id', db.Integer, primary_key=True)
    text_twit = db.Column('text_twit', db.String)
    person_id = db.Column(db.Integer)

    @property
    def json(self):
        return to_json(self, self.__class__)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'text_twit': self.text_twit,
            # This is an example how to deal with Many2Many relations
            'person_id': self.person_id
        }


class LikeTwitt(db.Model):
    __tablename__ = 'like_twit'

    person_id = db.Column('person_id', db.Integer, primary_key=True)
    twit_id = db.Column('twit_id', db.Integer, primary_key=True)
    # private
    # long
    # id;
    #
    # @NotNull
    # @NotBlank
    #
    # private
    # String
    # textTwit;
    #
    # @ManyToOne(fetch=FetchType.LAZY)
    # @JoinColumn(name="person_id", nullable=false)
    #
    # private
    # Person
    # author;
    # private
    # boolean
    # isPremium = false;
    #
    # @Column(insertable=true, updatable=false)
    #
    # private
    # LocalDateTime
    # created;
