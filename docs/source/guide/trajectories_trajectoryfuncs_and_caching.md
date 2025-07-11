# Trajectories, TrajectoryFunctions, and value caching

The {py:mod}`asyncmd.trajectory` module contains a {py:class}`Trajectory <asyncmd.Trajectory>` class which is the return object for all MD engines.
These objects enable easy access to a number properties of the underlying trajectory, like the length in frames or time, the integration step and many more.
Note that {py:class}`Trajectory <asyncmd.Trajectory>` are unique objects in the sense that every combination of underlying `trajectory_files` will give you the same object back even if you instantiate it multiple times, i.e. `is` will be `True` for the two objects (in addition to `==` being `True`).
Also note that it is possible to pickle and unpickle {py:class}`Trajectory <asyncmd.Trajectory>` objects.
You can even change the filepath of the underlying trajectories, i.e. copy/move them to another location (consider also moving the npz cache files) and still unpickle to get a working {py:class}`Trajectory <asyncmd.Trajectory>` object as long as the relative path between your python workdir and the trajectory files does not change. Or you can change the workdir of the python interpreter as long as the trajectory files remain at the same location in the filesystem.

asyncmd comes with a number of  {py:class}`TrajectoryFunctionWrapper <asyncmd.trajectory.functionwrapper.TrajectoryFunctionWrapper>` (sub)classes, which can be used to wrap (python) functions or arbitrary executables for easy concurrent application on {py:class}`Trajectory <asyncmd.Trajectory>` objects, either submitted via slurm or ran locally.
Currently included are the {py:class}`PyTrajectoryFunctionWrapper <asyncmd.trajectory.PyTrajectoryFunctionWrapper>` and the {py:class}`SlurmTrajectoryFunctionWrapper <asyncmd.trajectory.SlurmTrajectoryFunctionWrapper>`, but it is straightforward to implement your own (see [here for an in-depth explanation](#extending-asyncmd-trajectoryfunctions)).
The benefit of the wrapped functions is that the calculated values will be cached automatically.
The caching is even persistent over multiple reloads and invocations of the python interpreter.
To this end the default caching mechanism creates hidden numpy npz files for every {py:class}`Trajectory <asyncmd.Trajectory>` (named after the trajectory) in which the values are stored.
Other caching mechanism are an in-memory cache and the option to store all cached values in a {py:class}`h5py.File` or {py:class}`h5py.Group`.
You can set the default caching mechanism for all {py:class}`Trajectory <asyncmd.Trajectory>` objects centrally via {py:func}`asyncmd.config.set_default_trajectory_cache_type` or overwrite it for each {py:class}`Trajectory <asyncmd.Trajectory>` separately at init by passing ``cache_type``.

```{seealso}
The example notebooks on the {doc}`PyTrajectoryFunctionWrapper </examples_link/02_TrajectoryFunctionWrappers/PyTrajectoryFunctionWrapper>` and the {doc}`SlurmTrajectoryFunctionWrapper </examples_link/02_TrajectoryFunctionWrappers/SlurmTrajectoryFunctionWrapper>`.
```

```{seealso}
{py:func}`asyncmd.config.register_h5py_cache`, the function used to register the h5py cache.
```

```{seealso}
{py:func}`asyncmd.trajectory._forget_all_trajectories` and {py:func}`asyncmd.trajectory._forget_trajectory`, two helper functions to remove trajectories or a specific trajectory from the internal registry of trajectories.
```

## Trajectory

```{eval-rst}
.. autoclass:: asyncmd.Trajectory
    :class-doc-from: both
    :member-order: groupwise
    :members:
    :exclude-members: __new__, __getstate__, __eq__, __ne__, __repr__, __weakref__, __init__
    :special-members:
    :inherited-members:
```

## TrajectoryFunctionWrappers

```{eval-rst}
.. autoclass:: asyncmd.trajectory.PyTrajectoryFunctionWrapper
    :class-doc-from: both
    :member-order: groupwise
    :members:
    :exclude-members: __repr__, __weakref__, __init__
    :special-members:
    :inherited-members:
```

```{eval-rst}
.. autoclass:: asyncmd.trajectory.SlurmTrajectoryFunctionWrapper
    :class-doc-from: both
    :member-order: groupwise
    :members:
    :exclude-members: __repr__, __weakref__, __init__
    :special-members:
    :inherited-members:
```
