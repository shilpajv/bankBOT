import typing
from typing import Any, Optional, Text, Dict, List, Type

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.training_data.message import Message

from modules_helping import *

from rasa.nlu.extractors.extractor import EntityExtractor

from rasa.shared.nlu.constants import (
    ENTITIES,
    ENTITY_ATTRIBUTE_VALUE,
    ENTITY_ATTRIBUTE_START,
    ENTITY_ATTRIBUTE_END,
    TEXT,
    ENTITY_ATTRIBUTE_TYPE,
    EXTRACTOR
)

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


class NERv2(EntityExtractor):
   
    @classmethod
    def required_components(cls) -> List[Type[Component]]:
        

        return []

    
    defaults = {}

 
    supported_language_list = None

    
    not_supported_language_list = None

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super(NERv2,self).__init__(component_config)

    def train(
        self,
        training_data: TrainingData,
        config: Optional[RasaNLUModelConfig] = None,
        **kwargs: Any,
    ) -> None:
        
        pass
        

    def process(self, message: Message, **kwargs: Any) -> None:
        
        text = message.get('text',[])
        print("text:",text)
        user_values = get_user_values(text)
        print("user_values:",user_values)
        entities = []
        entities.append(
                    {
                        ENTITY_ATTRIBUTE_TYPE: 'abc',
                        ENTITY_ATTRIBUTE_START: None,
                        ENTITY_ATTRIBUTE_END: None,
                        ENTITY_ATTRIBUTE_VALUE: None,
                        EXTRACTOR : None,
                    })
        pass

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
      

        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any,
    ) -> "Component":
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)
