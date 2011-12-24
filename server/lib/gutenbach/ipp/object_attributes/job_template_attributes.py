__all__ = [
    'JobPriority',
    'JobHoldUntil',
    'JobSheets',
    'MultipleDocumentHandling',
    'Copies',
    'Finishings',
    'PageRanges',
    'Sides',
    'NumberUp',
    'OrientationRequested',
    'Media',
    'PrinterResolution',
    'PrintQuality',
]

from ..attribute import Attribute
from ..value import Value
from ..exceptions import ClientErrorAttributes

class JobPriority(Attribute):
    """4.2.1 job-priority (integer(1:100))

    This attribute specifies a priority for scheduling the Job. A
    higher value specifies a higher priority. The value 1 indicates
    the lowest possible priority. The value 100 indicates the highest
    possible priority. Among those jobs that are ready to print, a
    Printer MUST print all jobs with a priority value of n before
    printing those with a priority value of n-1 for all n.

    If the Printer object supports this attribute, it MUST always
    support the full range from 1 to 100. No administrative
    restrictions are permitted. This way an end-user can always make
    full use of the entire range with any Printer object. If
    privileged jobs are implemented outside IPP/1.1, they MUST have
    priorities higher than 100, rather than restricting the range
    available to end-users.

    If the client does not supply this attribute and this attribute is
    supported by the Printer object, the Printer object MUST use the
    value of the Printer object's 'job-priority-default' at job
    submission time (unlike most Job Template attributes that are used
    if necessary at job processing time).
    
    The syntax for the 'job-priority-supported' is also
    integer(1:100).  This single integer value indicates the number of
    priority levels supported. The Printer object MUST take the value
    supplied by the client and map it to the closest integer in a
    sequence of n integers values that are evenly distributed over the
    range from 1 to 100 using the formula:

        roundToNearestInt((100x+50)/n)

    where n is the value of 'job-priority-supported' and x ranges from
    0 through n-1.

    For example, if n=1 the sequence of values is 50; if n=2, the
    sequence of values is: 25 and 75; if n = 3, the sequence of values
    is: 17, 50 and 83; if n = 10, the sequence of values is: 5, 15,
    25, 35, 45, 55, 65, 75, 85, and 95; if n = 100, the sequence of
    values is: 1, 2, 3, ... 100.

    If the value of the Printer object's 'job-priority-supported' is
    10 and the client supplies values in the range 1 to 10, the
    Printer object maps them to 5, in the range 11 to 20, the Printer
    object maps them to 15, etc.

    """
    
    
    def __init__(self, val):
        super(type(self), self).__init__(
            'job-priority',
            [Value(IntegerTags.INTEGER), val])

class JobHoldUntil(Attribute):
    """4.2.2 job-hold-until (type3 keyword | name (MAX))
    
    """

    def __init__(self, val):
        raise ClientErrorAttributes, "job-hold-until"

class JobSheets(Attribute):
    """4.2.3 job-sheets (type3 keyword | name(MAX))

    """

    def __init__(self, val):
        raise ClientErrorAttributes, "job-sheets"

class MultipleDocumentHandling(Attribute):
    """4.2.4 multiple-document-handling (type2 keyword)

    """

    def __init__(self, val):
        raise ClientErrorAttributes, "multiple-document-handling"

class Copies(Attribute):
    """4.2.5 copies (integer(1:MAX))

    """

    def __init__(self, val):
        raise ClientErrorAttributes, "copies"

class Finishings(Attribute):
    """4.2.6 finishings (1setOf type2 enum)

    """

    def __init__(self, *vals):
        raise ClientErrorAttributes, "finishings"

class PageRanges(Attribute):
    """4.2.7 page-ranges (1setOf rangeOfInteger (1:MAX))

    """

    def __init__(self, *vals):
        raise ClientErrorAttributes, "page-ranges"

class Sides(Attribute):
    """4.2.8 sides (type2 keyword)

    """

    def __init__(self, val):
        raise ClientErrorAttributes, "sides"

class NumberUp(Attribute):
    """4.2.9 number-up (integer(1:MAX))

    """

    def __init__(self, val):
        raise ClientErrorAttributes, "number-up"

class OrientationRequested(Attribute):
    """4.2.10 orientation-requested (type2 enum)

    """

    def __init__(self, val):
        raise ClientErrorAttributes, "orientation-requested"

class Media(Attribute):
    """4.2.11 media (type3 keyword | name(MAX))

    """

    def __init__(self, val):
        raise ClientErrorAttributes, "media"

### XXX: we may want to repurpose this for bitrate?
class PrinterResolution(Attribute):
    """4.2.12 printer-resolution (resolution)

    """

    def __init__(self, val):
        raise ClientErrorAttributes, "printer-resolution"

class PrintQuality(Attribute):
    """4.2.13 print-quality (type2 enum)

    """

    def __init__(self, val):
        raise ClientErrorAttributes, "print-quality"