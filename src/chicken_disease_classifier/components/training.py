from src.chicken_disease_classifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path
from typing import List


class Training:
    def __init__(self, config:TrainingConfig):
        self.config = config
        self.model = None
        self.train_generator = None
        self.valid_generator = None

    def get_base_model(self):
        # Ensures the model is loaded fresh each time this is called
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

        self.model.compile(optimizer="Adam",loss="categorical_crossentropy",metrics=["accuracy"])
        
    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale=1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],  # Exclude color channels
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        if not path.suffix == '.keras':
            path = path.with_suffix('.keras')  # Ensure using the recommended format
        model.save(path)

    def train(self, callback_list: List[tf.keras.callbacks.Callback]):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        # Recompile the model to reset optimizer and other stateful elements
        self.model.compile(
            optimizer='adam',  # Consider extracting as a parameter if needed
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_data=self.valid_generator,
            validation_steps=self.validation_steps,
            callbacks=callback_list
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )

