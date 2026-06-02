package com.kuronami.oceanworld;

import com.kuronami.isekaiapi.api.Isekai;
import com.mojang.logging.LogUtils;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import org.slf4j.Logger;

@Mod(OceanWorld.MODID)
public final class OceanWorld {
    public static final String MODID = "ocean_world";
    public static final String VERSION = "1.0.0";
    public static final Logger LOGGER = LogUtils.getLogger();

    public OceanWorld(IEventBus modBus) {
        LOGGER.info("Ocean World v{} loading", VERSION);
        LOGGER.info("Ocean World: Isekai API facade ready (query={}, remap={})",
                Isekai.query().getClass().getSimpleName(),
                Isekai.remap().getClass().getSimpleName());
    }
}
