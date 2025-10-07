<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_3"/>
        <attribute name="authors" value="Admin"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 09:12:09 PM"/>
        <attribute name="created" value="QWRtaW47TEFQVE9QLVYyVDE1UFE3OzI1NjgtMDctMjI7MDk6MDc6MDEgUE07MjgyOQ=="/>
        <attribute name="edited" value="QWRtaW47TEFQVE9QLVYyVDE1UFE3OzI1NjgtMDctMjI7MDk6MTI6MDkgUE07MTsyOTQx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>