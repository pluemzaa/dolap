<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="1"/>
        <attribute name="authors" value="Nattakrit"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 01:36:33 PM"/>
        <attribute name="created" value="TmF0dGFrcml0O0xBUFRPUC1BTEVaRTsyMDI1LTA3LTE3OzAxOjI2OjM3IFBNOzMxMTE="/>
        <attribute name="edited" value="TmF0dGFrcml0O0xBUFRPUC1BTEVaRTsyMDI1LTA3LTE3OzAxOjM2OjMzIFBNOzI7MzIxNw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="s, e" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="s"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="e"/>
            <while expression="s&lt;e+1">
                <output expression="s" newline="True"/>
                <assign variable="s" expression="s+1"/>
            </while>
        </body>
    </function>
</flowgorithm>