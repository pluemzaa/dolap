<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_3"/>
        <attribute name="authors" value="ACER NITRO 5"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 12:50:01 AM"/>
        <attribute name="created" value="QUNFUiBOSVRSTyA1O0xBUFRPUC1FNDdERzVFTDsyNTY4LTA3LTIwOzEyOjQ1OjU0IFBNOzMxMTM="/>
        <attribute name="edited" value="QUNFUiBOSVRSTyA1O0xBUFRPUC1FNDdERzVFTDsyNTY4LTA3LTIwOzAxOjAyOjU1IFBNOzE7MzIxMw=="/>
        <attribute name="edited" value="QVNVUztMQVBUT1AtVEtNRTJEN0E7MjU2OC0wNy0yMTsxMjo1MDowMSBBTTsxOzI3NDU="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="snum, enum" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="snum"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="enum"/>
            <while expression="snum &lt;= enum">
                <output expression="snum" newline="True"/>
                <assign variable="snum" expression="snum+1"/>
            </while>
        </body>
    </function>
</flowgorithm>