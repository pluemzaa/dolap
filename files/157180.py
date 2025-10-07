<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="jaylab3"/>
        <attribute name="authors" value="windows"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 11:27:16 AM"/>
        <attribute name="created" value="d2luZG93cztMQVBUT1AtVVVIQTdEMk07MjU2OC0wNy0yMjsxMDoyMjowMyBBTTszMTE0"/>
        <attribute name="edited" value="d2luZG93cztMQVBUT1AtVVVIQTdEMk07MjU2OC0wNy0yMjsxMToyNzoxNiBBTTs2OzMyMzc="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <output expression="&quot;input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>