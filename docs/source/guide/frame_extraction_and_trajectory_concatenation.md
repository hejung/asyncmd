# Frame extraction and trajectory concatenation

## FrameExtractors

The module {py:mod}`asyncmd.trajectory.convert` contains a number of classes to extract arbitrary frames from {py:class}`Trajectory <asyncmd.Trajectory>` objects to easily (re)initialize MD simulations from these configurations.
All {py:class}`FrameExtractor <asyncmd.trajectory.convert.FrameExtractor>` subclasses share a common interface and differ only in the modification applied to the configuration before writing it out.
Currently implemented are:

- {py:class}`NoModificationFrameExtractor <asyncmd.trajectory.convert.NoModificationFrameExtractor>`
- {py:class}`InvertedVelocitiesFrameExtractor <asyncmd.trajectory.convert.InvertedVelocitiesFrameExtractor>`
- {py:class}`RandomVelocitiesFrameExtractor <asyncmd.trajectory.convert.RandomVelocitiesFrameExtractor>`

Implementing your own {py:class}`FrameExtractor <asyncmd.trajectory.convert.FrameExtractor>` subclass with a custom modification is as easy as subclassing the abstract base class {py:class}`FrameExtractor <asyncmd.trajectory.convert.FrameExtractor>` and overwriting its {py:meth}`FrameExtractor.apply_modification <asyncmd.trajectory.convert.FrameExtractor.apply_modification>` method.

```{note}
All {py:class}`FrameExtractor <asyncmd.trajectory.convert.FrameExtractor>` subclasses have an async version of their function doing the work ({py:meth}`FrameExtractor.extract <asyncmd.trajectory.convert.FrameExtractor.extract>` vs {py:meth}`FrameExtractor.extract_async <asyncmd.trajectory.convert.FrameExtractor.extract_async>`).
The awaitable version does exactly the same as its sync counterpart, just that it does so in a separate thread.
```

```{seealso}
The example notebook on {doc}`FrameExtractors </examples_link/03_trajectory_propagation_and_subtrajectory_extraction/FrameExtractors>`.
```

```{eval-rst}
.. autoclass:: asyncmd.trajectory.convert.FrameExtractor
    :class-doc-from: both
    :members:
    :inherited-members:

.. autoclass:: asyncmd.trajectory.convert.NoModificationFrameExtractor
    :class-doc-from: both
    :members:
    :exclude-members: extract, extract_async
    :inherited-members: asyncmd.trajectory.convert.FrameExtractor

.. autoclass:: asyncmd.trajectory.convert.InvertedVelocitiesFrameExtractor
    :class-doc-from: both
    :members:
    :exclude-members: extract, extract_async
    :inherited-members: asyncmd.trajectory.convert.FrameExtractor


.. autoclass:: asyncmd.trajectory.convert.RandomVelocitiesFrameExtractor
    :class-doc-from: both
    :members:
    :exclude-members: extract, extract_async
    :inherited-members: asyncmd.trajectory.convert.FrameExtractor
```

## Trajectory concatenation

The {py:mod}`asyncmd.trajectory.convert` module furthermore contains a class to
concatenate {py:class}`Trajectory <asyncmd.Trajectory>` segments, the {py:class}`TrajectoryConcatenator <asyncmd.trajectory.convert.TrajectoryConcatenator>`.
It can be used to concatenate lists of trajectory segments in any order (and possibly with inverted momenta) by passing a list of trajectory segments and a list of tuples (slices) that specify the frames to use in the concatenated output trajectory.
Note that this class gives you all customizability at the cost of complexity, if you just want to construct a transition from trajectory segments, the {py:func}`<construct_TP_from_plus_and_minus_traj_segments <asyncmd.trajectory.construct_TP_from_plus_and_minus_traj_segments>` function is most probably easier to use and what you want (it uses the {py:class}`TrajectoryConcatenator <asyncmd.trajectory.convert.TrajectoryConcatenator>` under the hood anyway).

```{note}
The {py:class}`TrajectoryConcatenator <asyncmd.trajectory.convert.TrajectoryConcatenator>` also has an async version of the function doing the work ({py:meth}`TrajectoryConcatenator.concatenate <asyncmd.trajectory.convert.TrajectoryConcatenator.concatenate>` vs {py:meth}`TrajectoryConcatenator.concatenate <asyncmd.trajectory.convert.TrajectoryConcatenator.concatenate_async>` respectively).
Similar to the {py:class}`FrameExtractor <asyncmd.trajectory.convert.FrameExtractor>` subclasses, the awaitable versions does exactly the same as its sync counterpart.
```

```{eval-rst}
.. autoclass:: asyncmd.trajectory.convert.TrajectoryConcatenator
    :class-doc-from: both
    :members:
    :inherited-members:
```
