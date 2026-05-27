package com.kuronami.deepseaworld;

import com.kuronami.isekaiapi.api.Isekai;
import com.mojang.logging.LogUtils;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import org.slf4j.Logger;

@Mod(DeepSeaWorld.MODID)
public final class DeepSeaWorld {
    public static final String MODID = "deep_sea_world";
    public static final String VERSION = "0.1.0";
    public static final Logger LOGGER = LogUtils.getLogger();

    public DeepSeaWorld(IEventBus modBus) {
        LOGGER.info("Deep Sea World v{} loading", VERSION);
        LOGGER.info("Deep Sea World: Isekai API facade ready (query={}, remap={})",
                Isekai.query().getClass().getSimpleName(),
                Isekai.remap().getClass().getSimpleName());
    }
}
