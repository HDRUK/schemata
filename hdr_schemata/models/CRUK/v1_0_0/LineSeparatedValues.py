from __future__ import annotations

from typing import Optional

from pydantic import ConfigDict, RootModel, constr


class LineSeparatedValues(RootModel[Optional[constr(pattern=r"([^\\r\\n]+)")]]):
    model_config = ConfigDict(title="LineSeparatedValues")
